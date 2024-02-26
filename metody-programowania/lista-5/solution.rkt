#lang racket

(require "props.rkt")
(provide falsifiable-cnf?)

(define (lit? f)
  (or (var? f)
      (and (neg? f)
           (var? (neg-subf f)))))

(define (lit-pos v)
  v)

(define (lit-neg v)
  (neg v))

(define (lit-var l)
  (if (var? l)
      l
      (neg-subf l)))

(define (lit-pos? l)
  (var? l))

(define (to-nnf f)
  (cond
   [(var? f)  (lit-pos f)]
   [(neg? f)  (to-nnf-neg (neg-subf f))]
   [(conj? f) (conj (to-nnf (conj-left f))
                    (to-nnf (conj-right f)))]
   [(disj? f) (disj (to-nnf (disj-left f))
                    (to-nnf (disj-right f)))]))

(define (to-nnf-neg f)
  (cond
   [(var? f)  (lit-neg f)]
   [(neg? f)  (to-nnf (neg-subf f))]
   [(conj? f) (disj (to-nnf-neg (conj-left f))
                    (to-nnf-neg (conj-right f)))]
   [(disj? f) (conj (to-nnf-neg (disj-left f))
                    (to-nnf-neg (disj-right f)))]))

(define (mk-cnf xss)
  (cons 'cnf xss))

(define (clause? f)
  (and (list? f)
       (andmap lit? f)))

(define (cnf? f)
  (and (pair? f)
       (eq? 'cnf (car f))
       (list? (cdr f))
       (andmap clause? (cdr f))))

(define (to-cnf f)
  (define (join xss yss)
    (apply append (map (lambda (xs) (map (lambda (ys) (append xs ys)) yss)) xss)))
  (define (go f)
    (cond
     [(lit? f)  (list (list f))]
     [(conj? f) (append (go (conj-left f))
                        (go (conj-right f)))]
     [(disj? f) (join (go (disj-left f))
                      (go (disj-right f)))]))
  (mk-cnf (go f)))

(define (falsifiable-cnf? f)
  (define (isContradiction ls)
    (lambda (x) 
      (if (neg? x)
          (member (second x) ls)
          (member (neg x) ls))))
  
  (define (eval-clause S)
    (define ls (remove-duplicates S))
    (cond
      [(null? ls) false]
      [(> (length (filter (isContradiction ls) ls)) 0) false]
      [else ls]))
  
  (define cnf (to-cnf (to-nnf f)))

  (define formula
    (let eval ([f (cdr cnf)])
      (if (null? f)
          false
          (if (eval-clause (car f))
              
              (eval-clause (car f))

              (eval [cdr f])))))

  (define (falsify-set ls)      
    (define (falsify lit)
      (if (neg? lit)
          (list (second lit) #t)
          (list lit #f)))
    (map falsify ls))

  (if formula
      (falsify-set formula)
      false))

(define (falsifiable? f)

  (define (gen-vals xs)
   (if (null? xs)
       (list null)
       (let*
            ((vss (gen-vals (cdr xs)))
             (x (car xs))
             (vst (map (lambda (vs) (cons (list x true) vs)) vss))
             (vsf (map (lambda (vs) (cons (list x false) vs)) vss)))
          (append vst vsf))))

  (define (search f)
      (cond
        [(var? f) (list f)]
        [(neg? f) (search (second f))]
        [else (append (search (second f)) (search (third f)))]))
  (define variables (remove-duplicates (search f)))

  (define (eval f vs)
    
    (define (sub f vs) (second (car (filter (lambda (x) (eq? (car x) f)) vs))))
    (cond
        [(var? f) (sub f vs)]
        [(neg? f) (not (eval (second f) vs))]
        [(conj? f) (and (eval (second f) vs) (eval (third f) vs))]
        [(disj? f) (or (eval (second f) vs) (eval (third f) vs))]))
  
  (let loop ([vals (gen-vals variables)])

    
    (if (null? vals)
        false
        (if (eval f (car vals))
            (loop [cdr vals])
            true))))
            

(define (test f)
  (display "CNF:")
  (display (time (falsifiable-cnf? f)))
  (displayln "")
  (display "Naive:")
  (display (time (falsifiable? f)))
  (displayln ""))
      
    
(define malo-zmiennych (disj (disj (disj (neg (conj (disj 'b (neg 'b)) (disj 'a (neg 'a)))) (conj 'a 'b)) (disj (neg (conj (disj 'b (neg 'b)) (disj 'a (neg 'a)))) (conj 'a 'b)))
                 (disj (disj (neg (conj (disj 'b (neg 'b)) (disj 'a (neg 'a)))) (conj 'a 'b)) (disj (neg (conj (disj 'b (neg 'b)) (disj 'a (neg 'a)))) (conj 'a 'b)))))

(define wiele-zmiennych (disj (disj (disj (neg (conj (disj 'a (neg 'b)) (disj 'c (neg 'd)))) (conj 'e 'f)) (disj (neg (conj (disj 'g (neg 'h)) (disj 'i (neg 'j)))) (conj 'k 'l)))
                 (disj (disj (neg (conj (disj 'm (neg 'n)) (disj 'o (neg 'p)))) (conj 'r 's)) (disj (neg (conj (disj 'b (neg 'a)) (disj 'b (neg 'a)))) (conj 'a 'b)))))


(test malo-zmiennych)  ;CNF jest znacznie wolniejszy
(test wiele-zmiennych) ;Kombinatoryczne podejscie jest znacznie wolniejsze

; Wniosek: Zamiana na CNF dla dużych formuł jest bardzo czasochłonna, ale test falsyfikowalności nie jest zależny od ilości różnych zmiennych zdaniowych.
; W przeciwieństwie do rozwiązania z CNF-em kombinatoryczne podejście błyskawicznie ewaluuje duże formuły, ale liczba powtórzeń tego procesu rośnie wykładniczo wraz z ilością różniących się parami zmiennych.
