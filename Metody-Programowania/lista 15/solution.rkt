#lang racket
(provide philosopher)

(define (philosopher dtable k)
  (define (eat fst scd)
    ((dtable 'pick-fork) (modulo fst 5))
    ((dtable 'pick-fork) (modulo scd 5))
    ((dtable 'put-fork) (modulo fst 5))
    ((dtable 'put-fork) (modulo scd 5)))
  (if (= k 0)
      (eat k (+ k 1))
      (eat (+ k 1) k)))