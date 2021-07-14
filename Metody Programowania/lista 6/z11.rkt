#lang racket

(provide (struct-out const) (struct-out binop) rpn->arith)

;; -------------------------------
;; Wyrazenia w odwr. not. polskiej
;; -------------------------------

(define (rpn-expr? e)
  (and (list? e)
       (pair? e)
       (andmap (lambda (x) (or (number? x) (member x '(+ - * /))))
               e)))

;; ----------------------
;; Wyrazenia arytmetyczne
;; ----------------------

(struct const (val)    #:transparent)
(struct binop (op l r) #:transparent)

(define (arith-expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r)
     (and (symbol? op) (arith-expr? l) (arith-expr? r))]
    [_ false]))

;; ----------
;; Kompilacja
;; ----------

(define (rpn->arith e)
  (let loop ([args '()] [input e])
    (if (null? input)
        (if (= (length args) 1)
            (car args)
            (error "Invalid input"))

        (cond
          [(number? (car input))
           (loop [cons (const (car input)) args] [cdr input])]
          [(member (car input) '(+ - * /))
             (loop [cons (binop (car input) (cadr args) (car args)) (cddr args)] [cdr input])]))))
    

; Mozesz tez dodac jakies procedury pomocnicze i testy
(define (test e)
  (if (and
       (rpn-expr? e)
       (arith-expr? (rpn->arith e)))
      (rpn->arith e)
      false))


(test '())
(test '(1))
;(test '(1 2))
(test '(1 2 - 3 *))
(test '(1 2 3 4 5 6 7 - - - - - -))
(test '(1 2 + 3 4 - 5 6 * 7 8 / + + +))
;(test '(1 2 3 +))
;(test '(+ 1 2))





