/*
 * UWAGA! W poniższym kodzie należy zawrzeć krótki opis metody rozwiązania
 *        zadania. Będzie on czytany przez sprawdzającego. Przed przystąpieniem
 *        do rozwiązywania zapoznaj się dokładnie z jego treścią. Poniżej należy
 *        wypełnić oświadczenie o samodzielnym wykonaniu zadania.
 *
 * Oświadczam, że zapoznałem(-am) się z regulaminem prowadzenia zajęć
 * i jestem świadomy(-a) konsekwencji niestosowania się do podanych tam zasad.
 *
 * Imię i nazwisko, numer indeksu: __________ __________, ______
 */

        .text
        .globl  cubef
        .type   cubef, @function

/*
 * W moim rozwiązaniu używam następującej techniki: ____ ____ ____ ____
 */

cubef:
 		# r11 to znak
		movq $0x80000000, %r8
		movq %rdi, %r11
		andq %r8, %r11

		# r10 to wykladnik
		movq $0x7F800000, %r8
		movq %rdi, %r10
		andq %r8, %r10
		leaq (%r10, %r10, 2), %r10
		sbb  $2130706432, %r10 # 254 * 2^23


		# rdi to mantysa
		movq $0x007FFFFF, %r8
		andq %r8, %rdi
		add  $0x00800000, %rdi


		# mantysa do szescianu
		movq %rdi, %rax
		mul %rdi
                movq %rax, %rdi
                ret
		mul %rdi
		movq %rax, %rdi # ?
                movq %rdx, %rax
                


		# rcx to liczba shiftow
		movq %rdx, %rcx 
		shrq $6, %rcx # rcx to wiodące 2 bity

		movq %rcx, %r8 
		shrq $1, %r8 # r8 to wiodący 1 bit

		xorq  %rcx, %r8
		andq  %r8, %rcx


		# guard + bity poza mantysa (rax to mantysa cubed) 
		shlq $10, %rax
		shrq %cl, %rax
		shlq $7, %rax


		# guard to r8   (G)
		movq %rax, %r8
		shrq $63, %r8

		# round to r9   (R)
		shlq $1, %rax  # rax nie ma już guard bitu
		movq %rax, %r9
		shrq $63, %r9

		# sticky to rax (S)
		neg  %rax
		sbb  %rax, %rax
		inc  %rax

		# zaokrąglenie to rax -- (R and S) or (R and G) <=> (G or S) and R
		orq  %r8, %rax
		andq %r9, %rax

                

		# scalanie rdx z rdi
		movq $0xFFFFFFFFFFFFFF00, %r8
		andq %r8, %rdi
		orq  %rdx, %rdi
		rorq $5, %rdi
		rorq %cl, %rdi
		shrq $41, %rdi

		
		# zaokrąglanie
		addq %rax, %rdi # rdi jest teraz mantysą
		movq $0x007FFFFF, %r8
		andq %r8, %rdi

		# poprawianie wykładnika (r10)
        movq $0x7F800000, %r8
        andq %r8, %r10

		# movq $0x100000000, %r8 # sad 2
		# addq %rcx, %r10
		# movq %r10, %rcx
		# andq %r8, %rcx
		# shlq $1, %r10
		# orq  %rcx, %r10
		

		# inf
		# movq %r10, %rcx
		# andq %r8, %rcx
		# shrq $31, %rcx # rcx to bit przepełnienia
		# 
		# movq $0x7FFFFFFF, %rax
		# mul %rcx
		# movq %rax, %rsi # rsi to przypadek inf
# 
		# neg %rcx
		# movq $1, %r8
		# and %r8, %rcx
# 
		# movq %rdi, %rax
		# mul %rcx # rax to antyprzypadek infa	
# 
		# orq %rsi, %rax


		# wynik
		# orq %r11, %rax
		# orq %r10, %rax
                # movq $0, %rax

	ret

        .size   cubef, .-cubef
