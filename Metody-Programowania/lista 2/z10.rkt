#lang racket

(provide cont-frac)

(define (cont-frac num den)
  
  (define (abs n)
    (if (< n 0)
        (- n)
        n))
  
  (define (dist n m)
    (abs (- n m)))
    
  
  (define (calc-iter n fst1 sec1 fst2 sec2 prev)
    (let* ([Dn (den n)]
           [Nn (num n)]
           [An (+ (* Dn fst1) (* Nn sec1))]
           [Bn (+ (* Dn fst2) (* Nn sec2))]
           [res (/ An Bn)])
    
      (if (< (dist prev res) 0.0001)
        
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

   (cont-frac N D))

;;(arctg 1)
;;(atan 1)
;;(cont-frac (lambda (x) 1) (lambda (x) 1))



   

  