#lang racket

(provide mergesort merge split)

(define (merge lis1 lis2)
  (let iter ([acc '()] [l1 lis1] [l2 lis2])
    
    (cond [(null? l1) (append acc l2)]
          [(null? l2) (append acc l1)]
          [(<= (car l1) (car l2)) (iter [append acc (list (car l1))] [cdr l1] l2)]
          [else (iter [append acc (list (car l2))] l1 [cdr l2])])))

(define (split lis)
  (let loop ([i 0] [l1 '()] [l2 lis])
    (if (= i (ceiling (/ (length lis) 2)))
        (cons l1 l2)
        (loop [+ i 1] [append l1 (list (car l2))] [cdr l2]))))


(define (mergesort L)
  (if (<= (length L) 1)
      L
      (let ([ls (split L)])
        (merge (mergesort (car ls)) (mergesort (cdr ls))))))


(require rackunit)

(define (test)

    (define (test-merge)
        (define (check first-list second-list)
            (let ([actual (merge first-list second-list)]
                  [expected (sort (append first-list second-list)
                                  (lambda (x y) (< x y)))])
                (check-equal? actual expected)))

        (check (list 1 1 1 1) (list 1 1 1 1))
        (check (list 1 3 5 7 9) (list 2 4 6 8 10))
        (check (list 1 3 5 7) (list 2 4 6 8 10))
        (check (list 1 3 5 7 9) (list 2 4 6 8))
        (check (list 1) (list 2))
        (check (list 1) null)
        (check null (list 2))
        (check null null))

    (define (test-split)
        (define (check list-to-split)
            (let* ([half-length (/ (length list-to-split) 2)]
                   [splitted (split list-to-split)]
                   [actual-left (length (car splitted))]
                   [expected-left (ceiling half-length)]
                   [actual-right (length (cdr splitted))]
                   [expected-right (floor half-length)])
                (check-equal? actual-left expected-left)
                (check-equal? actual-right expected-right)))

        (check (list 1 2 3 4 5 6 7 8 9 10))
        (check (list 1 2 3 4 5 6 7 8 9))
        (check (list 1 2))
        (check (list 1))
        (check null))

    (define (test-mergesort)
        (define (check list-to-sort)
            (let ([actual (mergesort list-to-sort)]
                  [expected (sort list-to-sort
                                  (lambda (x y) (< x y)))])
                (check-equal? actual expected)))

        (check (list 1 2 3 4 5 6 7 8 9 10))
        (check (list 10 9 8 7 6 5 4 3 2 1))
        (check (list 9 0 10.856 1 1 -6 2.233 4 1 -1.58 5 -7 1))
        (check (list 1 1 1 1 1 1 1 1 1 1))
        (check (list 2 1))
        (check (list 1))
        (check null))

    (test-merge)
    (test-split)
    (test-mergesort))

(test)
