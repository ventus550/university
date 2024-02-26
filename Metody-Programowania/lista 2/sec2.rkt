#lang racket

(define (cont-frac num den k)

  (define (cc num den k i)
    (define N (num i))
    (define D (den i))
  
    (if (= i k)
        0
        (/ N (+ D (cc num den k (+ i 1))))))
  (cc num den k 1))


;;(cont-frac ( lambda ( i ) 1.0) ( lambda ( i ) 1.0) 10)


(define (pi k)
  (define (sq x) (* x x))
  
  (+ 3
     (cont-frac (lambda (i) (sq (- (* i 2) 1))) (lambda (i) 6.0) k)))

;;(pi 31)



(define (atan-cf x k)
  (define (sq x) (* x x))

  (/ x (+ 1
          (cont-frac (lambda (i) (sq (* i x))) (lambda (i) (+ (* 2 i) 1)) k))))

(atan-cf 10.0 1000)
(atan 10.0)














  