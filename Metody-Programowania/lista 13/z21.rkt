#lang typed/racket
;; (define współpraca (list "Krystian Jasionek" "Piotr Dobiech"))
(provide parse typecheck)


(define-type Value (U Number Boolean))
(define-predicate value? Value)

(define-type EType (U 'real 'boolean))

(define-type Expr (U const binop var-expr let-expr if-expr))
(define-predicate expr? Expr)

(struct const ([val : Value]))
(struct binop ([op : Symbol] [l : Expr] [r : Expr]))
(struct var-expr ([id : Symbol]))
(struct let-expr ([id : Symbol] [e1 : Expr] [e2 : Expr]))
(struct if-expr ([eb : Expr] [e1 : Expr] [e2 : Expr]))

(define-type BinopConcr (List Symbol Concrete Concrete))
(define-predicate binop-concr? BinopConcr)

(define-type LetConcr (List 'let (List Symbol Concrete) Concrete))
(define-predicate let-concr? LetConcr)

(define-type IfConcr (List 'if Concrete Concrete Concrete))
(define-predicate if-concr? IfConcr)

(define-type BoolConcr (U 'true 'false))
(define-predicate bool-concr? BoolConcr)

(define-type Concrete (U Number BoolConcr Symbol LetConcr IfConcr BinopConcr))
(define-predicate concrete? Concrete)

(: parse (-> Concrete Expr))
(define (parse q)
  (cond
    [(number? q) (const q)]
    [(bool-concr? q) (if (eq? q 'true)
                         (const true)
                         (const false))]
    [(symbol? q) (var-expr q)]
    [(let-concr? q)
     (let-expr (first (second q))
               (parse (second (second q)))
               (parse (third q)))]
    [(if-concr? q)
     (if-expr (parse (second q))
              (parse (third q))
              (parse (fourth q)))]
    [(binop-concr? q)
     (binop (first q)
            (parse (second q))
            (parse (third q)))]))


(define-type TypeEnvList (Listof (Pairof Symbol (U EType #f))))

(struct environ ([xs : TypeEnvList]))

(define-type TypeEnvironment environ)
(define-predicate type-environment? TypeEnvironment)

(: env-empty TypeEnvironment)
(define env-empty (environ null))

(: env-add (-> Symbol (U EType #f) TypeEnvironment TypeEnvironment))
(define (env-add x t env)
  (environ (cons (cons x t) (environ-xs env))))

(: env-lookup (-> Symbol TypeEnvironment (U EType #f)))
(define (env-lookup x env)
  (: assoc-lookup (-> TypeEnvList (U EType #f)))
  (define (assoc-lookup xs)
    (cond [(null? xs) (error "Unknown identifier")]
          [(eq? x (car (car xs))) (cdr (car xs))]
          [else (assoc-lookup (cdr xs))]))
  (assoc-lookup (environ-xs env)))

(: binop-type (-> EType EType (-> (U EType #f) (U EType #f) (U EType #f))))
(define (binop-type operand-type true-type)
  (lambda (l r) (if (and (eq? l operand-type)
                         (eq? r operand-type))
                    true-type
                    #f)))

(: typecheck-env (-> Expr TypeEnvironment (U EType #f)))
(define (typecheck-env e env)
  (match e
    [(const n) (if (real? n)
                   'real
                   'boolean)]
    [(var-expr x) (env-lookup x env)]
    
    [(binop op l r) (let ([lv (typecheck-env l env)] [rv (typecheck-env r env)])
                      (cond
                        [(member op (list '+ '- '* '/ '%)) ((binop-type 'real 'real) lv rv)]
                        [(member op (list '= '> '>= '< '<=)) ((binop-type 'real 'boolean) lv rv)]
                        [(member op (list 'and 'or)) ((binop-type 'boolean 'boolean) lv rv)]
                        [else #f]))]
    
    [(let-expr x e1 e2) (let ([t (typecheck-env e1 env)])
                          (if (eq? t #f)
                              #f
                              (typecheck-env e2 (env-add x t env))))]
    
    [(if-expr e1 e2 e3) (let ([e1 (typecheck-env e1 env)]
                              [e2 (typecheck-env e2 env)]
                              [e3 (typecheck-env e3 env)])
                          
                          (if (and (eq? e1 'boolean) (eq? e2 e3)) e2 #f))]))
                              

(: typecheck (-> Expr (U EType #f)))
(define (typecheck expr)
  (typecheck-env expr env-empty))
































       











   