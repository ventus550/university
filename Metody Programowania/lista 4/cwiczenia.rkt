#lang racket

(require racket/draw)

(define (last-pair ls)
  (if (null? (cdr ls))
      (list (car ls))
      (last-pair (cdr ls))))

(last-pair '(1 2 3 4 8))


(define (same-parity . args)
  (filter (lambda (x) (= (modulo (list-ref args 0) 2) (modulo x 2))) args))

      
(same-parity 2 2 3 4 5 6 7)


(cons '(1 2 3) '('(2.5 3.5) '(1 2 3)))
