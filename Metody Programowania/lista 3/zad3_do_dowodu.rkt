#lang racket


(define (reverse-it ls)
  (define (revert new idx)
    (if (= idx 0)
        new
        (revert (append new (list (list-ref ls (- idx 1)))) (- idx 1))))

  (revert '() (length ls)))


(define (reverse-rec ls)
  (define (revert idx)
    (if (= idx 0)
        (list (list-ref ls 0))
        (append (list (list-ref ls idx)) (revert (- idx 1)))))

  (revert (- (length ls) 1)))




(reverse-it '(10 11 12 13 14 15))
(reverse-rec '(10 11 12 13 14 15))
    
  
    