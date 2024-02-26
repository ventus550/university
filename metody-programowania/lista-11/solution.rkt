#lang racket
;;Zadanie napisane we współpracy z Krystianem Jasionekiem i Cezarym Świtałą



(require racket/contract)

(provide
  (contract-out
    [with-labels with-labels/c]
    [foldr-map foldr-map/c]
    [pair-from pair-from/c]))

(provide
  with-labels/c
  foldr-map/c
  pair-from/c)

(define with-labels/c
  (parametric->/c [a b] (-> (-> a b) (listof a) (listof (cons/c b (cons/c a null?))))))

(define (with-labels p xs)
  (foldr
    (lambda (x y) (cons (list (p x) x) y)) null xs))





(define foldr-map/c
  (parametric->/c [x a t]
    (-> (-> x a (cons/c t a))
        a
        (listof x)
        (cons/c (listof t) a))))

(define (foldr-map f a xs)
  (define (iterate a xs ys)
    (if (null? xs)
        (cons ys a)
        (let [(p (f (car xs) a))]
          (iterate (cdr p)
                   (cdr xs)
                   (cons (car p) ys)))))
  (iterate a (reverse xs) null))






(define pair-from/c
  (parametric->/c [x fv gv] (-> (-> x fv) (-> x gv) (-> x (cons/c fv gv)))))

(define (pair-from f g)
  (lambda (x)
    (cons (f x)
          (g x))))