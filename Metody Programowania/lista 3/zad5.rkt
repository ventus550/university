#lang racket

(define (select-min L)
  (define mn (apply min L))

  (define (leftovers acc ls)
    (if (= (car ls) mn)
        (append acc (cdr ls))

        (leftovers (append acc (list (car ls))) (cdr ls))))
    
  (cons mn (leftovers '() L)))



(define (selection-sort L)
  (let sort ([s (select-min L)])
    (if (= (length s) 1)
        s
        (cons (car s) (sort [select-min (cdr s)])))))






(selection-sort '(2 1 2 3 4 9 1 99 0))