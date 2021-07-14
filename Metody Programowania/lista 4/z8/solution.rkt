#lang racket

(provide heapsort)
(require "leftist.rkt")

(define (heapsort L)
  (define heap
    (let build ([xs L] [heap empty-heap])
      (if (null? xs)
          heap
          (build [cdr xs] [heap-insert (make-elem (car xs) (car xs)) heap]))))

  (let res ([heap heap] [sorted null])
    (if (heap-empty? heap)
        sorted
        (res [heap-pop heap] [append sorted (list (elem-val (heap-min heap)))]))))