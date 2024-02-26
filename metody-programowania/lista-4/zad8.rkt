#lang racket


(define (inc n) (+ n 1))
;;; leftist heaps ( after Okasaki )
;; data representation

(define leaf 'leaf)
(define (leaf? h) (eq? 'leaf h))
(define (tagged-list? len-xs tag xs)
  (and (list? xs)
       (= len-xs (length xs))
       (eq? (first xs) tag)))

(define (hnode? h)
  (and (tagged-list? 5 'hnode h)
        (natural? (caddr h))))
          
(define (hnode-elem h)
  (second h))
(define (hnode-left h)
  (fourth h))
(define (hnode-right h)
  (fifth h))
(define (hnode-rank h)
  (third h))

(define (elem-priority x)
  (car x))

(define (elem-val x)
   (cdr x))

(define (hord? p h)
  (or (leaf? h)
      (<= p (elem-priority (hnode-elem h)))))

(define (heap? h)
  (or (leaf? h)
      (and (hnode? h)
           (heap? (hnode-left h))
           (heap? (hnode-right h))
           (<= (rank (hnode-right h))
               (rank (hnode-left h)))
           (= (rank h) (inc (rank (hnode-right h))))
           (hord? (elem-priority (hnode-elem h))
                  (hnode-left h)))))

(define (rank h)
  (if (leaf? h)
      0
      (hnode-rank h)))

(define empty-heap leaf)
(define (heap-empty? h)
  (leaf? h))
(define (heap-insert elt heap)
  (heap-merge heap (make-hnode elt leaf leaf)))
(define (heap-min heap)
  (hnode-elem heap))
(define (heap-pop heap)
  (heap-merge (hnode-left heap) (hnode-right heap)))


;;----------------------------------------------------

(define (make-hnode elem heap-a heap-b)
  (let ([a-rank (rank heap-a)] [b-rank (rank heap-b)])
    (append
     (list 'hnode elem (inc (min a-rank b-rank)))
     (if (>= a-rank b-rank)
         (list heap-a heap-b)
         (list heap-b heap-a)))))

(define (heap-merge h1 h2)
  (cond
    [(heap-empty? h1) h2]
    [(heap-empty? h2) h1]
    [else (let* ([get (lambda (</> f) (if (</> (elem-priority (heap-min h1)) (elem-priority (heap-min h2))) (f h1) (f h2)))]
                [e  (get <= heap-min)]
                [hl (get <= hnode-left)]
                [hr (get <= hnode-right)]
                [h (get > (lambda (x) x))])
          (make-hnode e hl (heap-merge hr h)))]))

(define (heapsort L)
  (define heap
    (let build ([xs L] [heap empty-heap])
      (if (null? xs)
          heap
          (build [cdr xs] [heap-insert (car xs) heap]))))
  (displayln heap)
  (displayln (heap? heap))


  (let res ([heap heap] [sorted null])
    (if (heap-empty? heap)
        sorted
        (res [heap-pop heap] [append sorted (list (heap-min heap))]))))

(define (heaptest ls)
  (define pairs
    (let build ([xs ls] [pairs '()])
      (if (null? xs)
          pairs
          (build [cdr xs] [append pairs (list (cons (car xs) (car xs)))]))))

  (heapsort pairs))


(heaptest '(1 0 1 0 1 0 1))

    
    