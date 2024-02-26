#lang racket


(provide nth-root)

(define (close-to? x y)
  (< (abs (- x y)) 0.00001))


(define (fixed-point s f)
  (if (close-to? s (f s))
      s
      (fixed-point (f s) f)))


(define (average-damp-n f n)
  
  (define (average x y)
    (/ (+ x y) 2))

  (define (average-damp f)
    (lambda (x)
      (average x (f x))))
  
  (define (compose f g)
    (lambda (x) (f (g x))))
  
  (define (identity x) x)
  
  (define (repeated p n)
    (if (> n 0)
        (compose p (repeated p (- n 1)))
        identity))

  
  ((repeated average-damp n) f))



(define (nth-root n x)

  (define (pow num p)
    (define (pow-it acc p)
      (if (= p 0)
        acc
        (pow-it (* acc num) (- p 1))))
    (pow-it 1 p))
  
  (define calc
    (let ([op (lambda (y) (/ (abs x) (pow y (- n 1))))])
        (fixed-point 1.0 (average-damp-n op (floor (log n 2))))))

  (cond [(and (= (modulo n 2) 0) (< x 0)) (error "illegal arguments")]
        [(= x 0) 0]
        [(< x 0) (- calc)]
        [(> x 0) calc]))



(define (sqrt-test index damps)
  
  (define (pow num p)
    (define (pow-it acc p)
      (if (= p 0)
        acc
        (pow-it (* acc num) (- p 1))))
    (pow-it 1 p))


  (let ([op (lambda (y) (/ (pow 2 index) (pow y (- index 1))))])
    (display "Stopień pierwiastka: ")
    (displayln index)
    (fixed-point 1.0 (average-damp-n op damps))))

;;----------------------Testy-----------------------
;;testy pierwiastka z 2 dla różnych stopni i ilości tłumień:
(sqrt-test 2 1)
(sqrt-test 3 1)
;;(sqrt-test 4 1) <- pętla

(sqrt-test 4 2)
(sqrt-test 5 2)
(sqrt-test 6 2)
(sqrt-test 7 2)
;;(sqrt-test 8 2) <- petla

(sqrt-test 8 3)
(sqrt-test 9 3)
(sqrt-test 10 3)
(sqrt-test 11 3)
(sqrt-test 12 3)
(sqrt-test 13 3)
(sqrt-test 14 3)
(sqrt-test 15 3)
;;(sqrt-test 16 3) <- petla


;;zalezność wydaje się być logarytmiczna
;;dokładniej jest to logarytm o podstawie 2 z stopnia pierwiastka

;;testy na poprawionej funkcji
(displayln "------nth-root-------")
(nth-root 8 256)
(nth-root 100 200)
(nth-root 2 81)
(nth-root 3 0)
























