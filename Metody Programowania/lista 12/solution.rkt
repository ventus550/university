#lang racket
;;Zadanie napisane we współpracy z Krystianem Jasionekiem i Cezarym Świtałą

(require "graph.rkt")
(provide bag-stack@ bag-fifo@)

;; struktura danych - stos
(define-unit bag-stack@
  (import)
  (export bag^)

  (define (bag? b) (and (list? b)
                        (= (length b) 2)
                        (eq? (first b) 'stack)
                        (list? (second b))))

  (define (stack-list b) (second b))
  (define (stack-cons l) (list 'stack l))
  
  (define empty-bag (list 'stack '()))
  (define (bag-empty? b) (empty? (stack-list b)))
  (define (bag-insert b e) (stack-cons (cons e (stack-list b))))
  (define (bag-peek b) (first (stack-list b)))
  (define (bag-remove b) (stack-cons (cdr (stack-list b))))
)

;; struktura danych - kolejka FIFO
(define-unit bag-fifo@
  (import)
  (export bag^)

  (define (bag? f) (and (list? f)
                        (= (length f) 3)
                        (eq? (first f) 'fifo)
                        (list? (second f))
                        (list? (third f))))

  (define (fin f) (second f))
  (define (fout f) (third f))
  (define (fifo-cons l1 l2) (list 'fifo l1 l2))

  (define empty-bag (fifo-cons '() '()))
  (define (bag-empty? f) (and (empty? (fin f))
                              (empty? (fout f))))
  (define (bag-insert f e) (fifo-cons (cons e (fin f))
                                      (fout f)))
  (define (bag-peek f) (cond
                         [(empty? (fout f)) (first (reverse (fin f)))]
                         [(first (fout f))]))
  (define (bag-remove f) (cond
                           [(empty? (fout f)) (fifo-cons '() (cdr (reverse (fin f))))]
                           [else (fifo-cons (fin f) (cdr (fout f)))]))
)

;; otwarcie komponentów stosu i kolejki

(define-values/invoke-unit bag-stack@
  (import)
  (export (prefix stack: bag^)))

(define-values/invoke-unit bag-fifo@
  (import)
  (export (prefix fifo: bag^)))

;; testy w Quickchecku
(require quickcheck)

;; testy kolejek i stosów
(define-unit bag-tests@
  (import bag^)
  (export)
  
  ;; test przykładowy: jeśli do pustej struktury dodamy element
  ;; i od razu go usuniemy, wynikowa struktura jest pusta


  (quickcheck
   (property ([any-symbol arbitrary-symbol])
             (eq? any-symbol (bag-peek (bag-insert empty-bag any-symbol)))))
  (quickcheck
   (property ([any-symbol arbitrary-symbol])
             (bag-empty? (bag-remove (bag-insert empty-bag any-symbol)))))
  (quickcheck
   (property ([any-symbol arbitrary-symbol]) 
             (not (empty? (bag-insert empty-bag any-symbol)))))
  (quickcheck
   (property ([any-symbol arbitrary-symbol])
             (bag? (bag-insert empty-bag any-symbol))))
)

(define-unit fifo-tests@
  (import bag^)
  (export)


  (quickcheck
   (property
    ([s1 arbitrary-symbol]
     [s2 arbitrary-symbol])
    (eq? s2 (bag-peek (bag-remove (bag-insert (bag-insert empty-bag s1) s2))))))

  (quickcheck
   (property
    ([s1 arbitrary-symbol]
     [s2 arbitrary-symbol])
    (eq? s1 (bag-peek (bag-insert (bag-insert empty-bag s1) s2)))))

  
)

(define-unit stack-tests@
  (import bag^)
  (export)


  (quickcheck
   (property
    ([s1 arbitrary-symbol]
     [s2 arbitrary-symbol])
    (eq? s1 (bag-peek (bag-remove (bag-insert (bag-insert empty-bag s1) s2))))))

  (quickcheck
   (property
    ([s1 arbitrary-symbol]
     [s2 arbitrary-symbol])
    (eq? s2 (bag-peek (bag-insert (bag-insert empty-bag s1) s2)))))

  
)

;; uruchomienie testów dla obu struktur danych

(invoke-unit bag-tests@ (import (prefix stack: bag^)))
(invoke-unit bag-tests@ (import (prefix fifo: bag^)))

(invoke-unit stack-tests@ (import (prefix stack: bag^)))
(invoke-unit fifo-tests@ (import (prefix fifo: bag^)))


;; TODO: napisz też testy własności, które zachodzą tylko dla jednej
;; z dwóch zaimplementowanych struktur danych

;; otwarcie komponentu grafu
(define-values/invoke-unit/infer simple-graph@)

;; otwarcie komponentów przeszukiwania 
;; w głąb i wszerz
(define-values/invoke-unit graph-search@
  (import graph^ (prefix stack: bag^))
  (export (prefix dfs: graph-search^)))

(define-values/invoke-unit graph-search@
  (import graph^ (prefix fifo: bag^))
  (export (prefix bfs: graph-search^)))

;; graf testowy
(define test-graph
  (graph
   (list 1 2 3 4)
   (list (edge 1 3)
         (edge 1 2)
         (edge 2 4))))

(define test-graph_1
  (graph
   (list 4 3 2 1 0)
   (list (edge 1 3)
         (edge 1 2)
         (edge 2 4)
         (edge 0 1))))

(define test-graph_2
  (graph
   (list 1 2 3 4 5 6 7 8 9 10)
   (list (edge 1 3)
         (edge 1 2)
         (edge 2 4)
         (edge 4 5)
         (edge 5 6)
         (edge 6 7)
         (edge 7 8)
         (edge 8 9))))

(define test-graph_3
  (graph
   (list 1 2)
   (list (edge 1 2)
         (edge 2 1))))




;; uruchomienie przeszukiwania na przykładowym grafie
(bfs:search test-graph 1)
(dfs:search test-graph 1)


;; Inne grafy - testy
(bfs:search test-graph_1 1)
(dfs:search test-graph_1 1)

(bfs:search test-graph_2 1)
(dfs:search test-graph_2 1)

(bfs:search test-graph_3 1)
(dfs:search test-graph_3 1)
