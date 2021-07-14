#lang racket


(struct binop (op l r))
(struct const (val))

(define (pretty-print f)
  (define (listify val)
    (if (list? val)
        val
        (list val)))

  (match f
    [(const n) n]
    [(binop op l r)
     (cond
       [(or (eq? op '+) (eq? op '-)) (append (listify (pretty-print l)) (list op) (listify (pretty-print r)))]
       [else (list (pretty-print l) op (pretty-print r))])] ;prawie dobrze
    [_ false]))
    
