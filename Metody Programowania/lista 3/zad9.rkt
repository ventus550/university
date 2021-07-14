#lang racket

(provide partition quicksort)

(define (partition n xs)
  (let loop ([l1 '()] [l2 '()] [curr xs])
    (if (null? curr)
        (cons l1 l2)

        (if (<= (car curr) n)
            (loop [append l1 (list (car curr))] l2 [cdr curr])
            (loop l1 [append l2 (list (car curr))] [cdr curr])))))

(define (quicksort L)
  (if (<= (length L) 1)
      L
      (let ([p (partition (car L) (cdr L))])
        (append (quicksort (car p)) (list (car L)) (quicksort (cdr p))))))


