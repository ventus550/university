#lang racket

(define (z4 a b c)
  (let ([x (max a b)] [y (max b c)] [z (max a c)] [sq (lambda (n m) (+ (* n n) (* m m)))] )
    (cond [(<= x c) (sq x c)]
          [(<= y a) (sq y a)]
          [(<= z b) (sq z b)]
          [else -1])))
  
(define (func)
    (define a 3)
    (define b 3)
    (+ a b))

(define (z8 b n)
  (let loop ([i 0])
    (if (> (expt b i) n)
        i
        (loop (+ i 1)))))

                         



(define (power-close-to b n)

  (define <>
    (if (< b 1)
        >
        <))
  
  (define (loop i)
    (if (<> (expt b i) n)
        (loop (+ i 1))

        (if (<> (expt b (- i 1)) n)
           i
           (loop (- i 1)))))


  (if (= b 1) (/ 0 0) (loop 0)))


(power-close-to (- (/ 1 2)) (/ 1 100) )

  
