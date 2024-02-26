/*
 * UWAGA! W poniższym kodzie należy zawrzeć krótki opis metody rozwiązania
 *        zadania. Będzie on czytany przez sprawdzającego. Przed przystąpieniem
 *        do rozwiązywania zapoznaj się dokładnie z jego treścią. Poniżej należy
 *        wypełnić oświadczenie o samodzielnym wykonaniu zadania.
 *
 * Oświadczam, że zapoznałem(-am) się z regulaminem prowadzenia zajęć
 * i jestem świadomy(-a) konsekwencji niestosowania się do podanych tam zasad.
 *
 * Imię i nazwisko, numer indeksu: Jakub Skalski, 314007
 */

		.data
		mask: .quad 0x0f0f0f0f0f0f0f0f
        .text
        .globl  mod17
        .type   mod17, @function
		
		

/*
 * W moim rozwiązaniu używam następującej techniki: 
	Zaczynam od podziału liczby na jej parzyste i nieparzyste wektory cyfry, które następnie sumuję.
	Zgodnie z wskazówką mod17 różnicy tych wektorów jest taki jak dla pierwotnej liczby.
	Można łatwo sprawdzić, że powstała w ten sposób liczba jest z przedziału [-120, 120].
	Dla liczb dodatnich wystarczy powtórzyć powyższy proces dla pojedynczego bajtu.
	Liczby z przedziału ujemnego są kłopotliwe, ale możemy sobie z nimi poradzić.
	Zauważmy, że dodanie 136 (jako, że 136 mod 17 to 0) nie wpływa na ostateczny wynik, zatem
	wystarczy dodać 136 do liczby ujemnej, aby przywrócić ją do wygodnego w obliczeniach zakresu liczb dodatnich.
	W ostatnim kroku powstaje nam nowa liczba i po raz kolejny może ona być ujemna i radzimy sobie z nią w podobny sposób
	co powyżej tym razem dodając 17.
 */

mod17:
	# dzielimy cyfry na parzyste i nieparzyste
	movq	%rdi, %rdx   # optymalizacja ICP
	movq    %rdx, %rax
    andq    (mask), %rdx # rdx to parzyste

    shrq    $4, %rax
    andq    (mask), %rax # rax to nieparzyste


    # sumowanie

    # sumy czworek
    movq %rdx, %rsi
    shrq $8, %rsi
    addq %rsi, %rdx

    movq %rax, %rcx
    shrq $8, %rcx
    addq %rcx, %rax


    # sumy osemek
    movq %rdx, %rsi
    shrq $16, %rsi
    addq %rsi, %rdx

    movq %rax, %rcx
    shrq $16, %rcx
    addq %rcx, %rax


    # sumy szesnastek
    movq %rdx, %rsi
    shrq $32, %rsi
    addq %rsi, %rdx

    movq %rax, %rcx
    shrq $32, %rcx
    addq %rcx, %rax

    # odejmujemy nieparzyste (rax) od parzystych (rdx)
    subq	%rax, %rdx
	cmpq	$0, %rax
	leaq	136(%rdx), %rax
	cmova	%rax, %rdx

	# to samo co wyżej ale dla liczby długości 1 bajtu
	movq	%rdx, %rax
	shrq	$4, %rdx
	andl	$0xF, %edx
	andl	$0xF, %eax

	subq	%rdx, %rax
	leaq	17(%rax), %rdx
	cmovl	%rdx, %rax
    
    ret
        .size   mod17, .-mod17
