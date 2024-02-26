#lang racket

(define (calc Di Ni)
  
  (define (abs n)
    (if (< n 0)
        (- n)
        n))
  
  (define (dist n m)
    (abs (- n m)))
    
  
  (define (calc-iter n fst1 sec1 fst2 sec2 prev)
    (let* ([Dn (Di n)]
           [Nn (Ni n)]
           [An (+ (* Dn fst1) (* Nn sec1))]
           [Bn (+ (* Dn fst2) (* Nn sec2))]
           [res (/ An Bn)])
    
      (if (< (dist prev res) 0.00001)
        
          res

          (calc-iter (+ n 1) An fst1 Bn fst2 res))))

  (calc-iter 1 0.0 1.0 1.0 0.0 0))

(define (arctg x)
  (define (N i)
    (if (= i 1)
        x
        (* (* (- i 1) x) (* (- i 1) x))))

   (define (D i)
     (- (* 2 i) 1))

   (calc D N))
(arctg 1)
(atan 1)
