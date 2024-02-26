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

        .text
        .globl  clz
        .type   clz, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
        Przypuśćmy, że potrafimy wypełnić luki między jedynkami w taki sposób, że tylko zera wiodące pozostają nieruszone (przykładowo 000101100100 -> 000111111111).
        Mozna łatwo zauważyć, że problem redukuje się do policzenia wszystkich zer. W tym celu możemy wykorzystać pokazany na ćwiczeniach algorytm popcount
        zliczający wszystkie zapalone bity danej liczby. Jak wiemy działa on w czasie O(logn). W takim razie wystarczy tylko zanegować naszą liczbę i wykonać
        na niej wspomniany algorytm.
        Pozostaje jeszcze kwestia szybkiego wypełniania luk. Szczęśliwie jest to raczej prosta czynność polegająca na "rozsmarowaniu" wiodącej jedynki, czyli
        wielokrotnym użyciu instrukcji `shrq` oraz `orq` w sposób gwarantujący zapalenie wszystkich następujących po tej jedynce bitów:
        000100000000 -> 000110000000 -> 000111100000 -> 000111111110 -> 000111111111 (oczywiście, wszystkie niewiodące jedynki nie wpływają na efekt końcowy) 
 */

clz:
	# Wypełnianie luk
	movq	%rdi, %rax
	shrq	%rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$2, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$4, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$8, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$16, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$32, %rdi
	orq		%rdi, %rax

	notq	%rax

        # Popcount
	movq    $0x5555555555555555, %rcx
	movq	%rax, %rdi
	shrq	%rdi
	andq	%rcx, %rdi
	subq	%rdi, %rax

	movq    $0x3333333333333333, %rcx
	movq	%rax, %rdi
	shrq	$2, %rdi
	andq	%rcx, %rdi
	andq	%rcx, %rax
	addq	%rdi, %rax

	movq    $0x0f0f0f0f0f0f0f0f, %rcx
	movq	%rax, %rdi
	shrq	$4, %rdi
	addq	%rdi, %rax
	andq	%rcx, %rax

    movq	%rax, %rdi
	shrq	$8, %rdi
	addq	%rdi, %rax

    movq	%rax, %rdi
	shrq	$16, %rdi
	addq	%rdi, %rax

    movq	%rax, %rdi
	shrq	$32, %rdi
	addq	%rdi, %rax

    movq    $0x000000000000007F, %rcx
    andq    %rcx, %rax
	
	
	ret

        .size   clz, .-clz
