#lang racket


(define (insert xs n)
  (let iter ([i -1] [ls '()] [not-inserted #t])
    
    (if (= i (- (length xs) 1))
        
        (if not-inserted
            
           (append ls (list n))
           
           ls)
            
        (let ([next (list-ref xs (+ i 1))])
          (if (and (<= n next) not-inserted)

              (iter [+ i 1] [append ls (list n next)] #f)

              (iter [+ i 1] [append ls (list next)] not-inserted))))))


(define (insertion-sort l)
    (define (sort l acc)
      (if (null? l)
        acc
        (sort (cdr l) (insert acc (car l)))))
    (sort l '()))

(insertion-sort '(1 2 1 5 2 7 2))

(insert '() '(1))

'(1 2 3 '(1 2 3 '( 1 2 3)))