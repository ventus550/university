#lang racket

(struct const (val)    #:transparent)
(struct binop (op l r) #:transparent)
(define i 'i)
(struct complex (re im) #:transparent)
(define value? complex?)

; 2 + 2 * 2
(define 2+2*2 (binop '+ (const 2)
                        (binop '* (const 2)
                                  (const 2))))


; Co to są wyrażenia?
(define (expr? e)
  (match e
    [(const n) (number? n)]
    [(binop op l r) (and (symbol? op) (expr? l) (expr? r))]
    [_ false]))


(define (op->proc op)
  (define (sq n) (* n n))
  (lambda (x y)
    (let ([rx (complex-re x)] [ix (complex-im x)] [ry (complex-re y)] [iy (complex-im y)])
    (match op
      ['+ (complex (+ rx ry) (+ ix iy))]
      ['- (complex (- rx ry) (- ix iy))]
      ['* (complex (- (* rx ry) (* ix iy)) (+ (* rx iy) (* ry ix)))]
      ['/ (let ([cpx ((op->proc '*) x (complex (- ry) iy))]
                [divisor (- (+ (sq ry) (sq iy)))])
            
            (displayln x)
            (displayln (complex ry (- iy)))
            (displayln cpx)
            (displayln divisor)
            (complex (/ (complex-re cpx) divisor) (/ (complex-im cpx) divisor)))]))))
        

(define (eval e)
  (match e
    [(complex re im) (complex re im)]
    [(binop op l r) ((op->proc op) (eval l) (eval r))]))

; ------------------------- ;
; Trochę składni konkretnej ;
; ------------------------- ;

(define (parse q)
  (cond [(number? q) (complex q 0)]
        [(eq? 'i q) (complex 0 1)]
        [(and (list? q) (eq? (length q) 3) (symbol? (first q)))
         (binop (first q) (parse (second q)) (parse (third q)))]))

(eval (parse '(/ (+ (* 8 i) 10) (+ (* 2 i) 3))))
(eval (parse '(* (+ (* 8 i) 10) (- (* 2 i) 3))))







































