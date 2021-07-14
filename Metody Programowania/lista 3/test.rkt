#lang racket

(define (point? p)
  (and (number? x) (number? y)))

(define (if-point-then p f)
  (if (and (point? (car p)) (point? (cdr p)))
      (f p)
      (error "Illiegal argument")))

(define (make-point x y)
  (if-point-then (cons x y) (lambda (x) x)))

(define (point-x p)
  (if-point-then p (car p)))

(define (point-y p)
  (if-point-then p (cdr p)))



(define (vect? v)
  (and (point? x) (point? y)))

(define (if-vect-then v f)
  (if (and (point? (car v)) (point? (cdr p)))
      (f v)
      (error "Illiegal argument")))

(define (make-vect p q)
  (if-vect-then (cons p q) (lambda (x) x)))

(define (vect-begin v)
  (if-vect-then v (car v)))

(define (vect-end v)
  (if-vect-then v (cdr v)))


