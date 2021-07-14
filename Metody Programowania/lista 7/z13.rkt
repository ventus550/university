#lang racket
(provide (struct-out const) (struct-out binop)
         (struct-out var-expr) (struct-out let-expr)
         (struct-out var-dead) find-dead-vars)

; --------- ;
; Wyrazenia ;
; --------- ;

(struct const    (val)      #:transparent)
(struct binop    (op l r)   #:transparent)
(struct var-expr (id)       #:transparent)
(struct var-dead (id)       #:transparent)
(struct let-expr (id e1 e2) #:transparent)

(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [(var-expr x) (symbol? x)]
    [(var-dead x) (symbol? x)]
    [(let-expr x e1 e2) (and (symbol? x) (expr? e1) (expr? e2))]
    [_ false]))

(define (parse q)
  (cond
    [(number? q) (const q)]
    [(symbol? q) (var-expr q)]
    [(and (list? q) (eq? (length q) 3) (eq? (first q) 'let))
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))

; ---------------------------------- ;
; Wyszukaj ostatnie uzycie zmiennych ;
; ---------------------------------- ;





(define (find-dead-vars e)

  (struct res (exp env) #:transparent)
  (struct pair (id type) #:transparent)

  (define (erase-id id env)
    (let loop ([this (car env)] [rest (cdr env)])
      (cond
        [(eq? this null) (error "#404")]
        [(eq? (pair-id this) id)
         (if (eq? (pair-type this) 'bound)
             (loop [car rest] [cdr rest])
             rest)]
        [else (cons this (loop [car rest] [cdr rest]))])))

  (define (dead-check v env)
    (let loop ([env env])
      (cond
        [(eq? env null) (error " #404")]
        [(eq? (pair-id (car env)) v)
         (if (eq? (pair-type (car env)) 'bound)
             (var-expr v)
             (var-dead v))]
        [else (loop [cdr env])])))            

  (define (dead-rec e env)
    (match e
      [(const n) (res (const n) env)]
      [(binop op l r)
       (let* ([right (dead-rec r env)] [left (dead-rec l (res-env right))])
         (res (binop op
                      (res-exp left)
                      (res-exp right))
               (res-env left)))]
      [(var-expr x) (res (dead-check x env) (cons (pair x 'bound) env))]
      [(let-expr x e1 e2)
       (let* ([right (dead-rec e2 (cons (pair x 'binding) env))] [left (dead-rec e1 (erase-id x (res-env right)))])
         (res (let-expr x
                   (res-exp left)
                   (res-exp right))
               (res-env left)))]
      [_ false]))


  (res-exp (dead-rec e '())))












