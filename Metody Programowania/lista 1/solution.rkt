#lang racket
(provide cube-root)
(provide cube)

;;kod mocno inspirowany wykładem


(define (cube x)
  (* x x x))


(define (cube-root x)

  (define (average z y)
  (/ (+ z y) 3))

  (define (dist x y)
    (abs (- x y)))

  (define (abs x)
    (if (< x 0)
        (- x)
        x))
  
  (define (improve guess)
    (average (* 2 guess) (/ x (* guess guess))))

  
  (define (good-enough? g)
    (< (dist x (cube g))
       0.000000000001))

  
  (define (iter guess)
    (if (good-enough? guess)
        guess
        (iter (improve guess))))
  
  (iter 1.0))

(cube-root (cube (/ 1 2)))
(cube-root (cube 631))
(cube-root (cube 0.99999999))
(cube (cube-root 10))
