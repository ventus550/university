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
                sgn: .long 0x80000000
                mantysa: .long 0x007FFFFF
                exp: .long 0x7F800000
                merge: .quad 0xFFFFFFFFFFFFFF00
                zero: .quad 0x0
        .text
        .globl  cubef
        .type   cubef, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
        Zaczynamy od podzielenia wejściowej liczby na znak, wykładnik i mantysę.
        Znak się nie zmienia i jest przepisywany na końcu działania programu.
        Wykładnik jest mnożony przez trzy. Od tego wyniku odejmowana jest dwukrotność biasu.
        Podniesiona do sześcianu mantysa zostanie rozmazana po rejestrach RDX:RAX (umowna jedynka bierze udział w obliczeniach).
        Zauważmy, że część całkowita zajmuje bity 70, 71, 72, zatem normalizujemy shiftując i inkrementując wykładnik o liczbę
        zapalonych bitów na pozycjach 71 i 72. Zapamiętujemy tą liczbę i używamy jej do wyznaczenia zakresów, z których należy
        wyciągać guard, round i sticky bity. Następnie wystarczy zaokrąglić mantyse wg. zasad dopełnienia do dwóch.
        Ostatecznie wystarczy złączyć w całość znak, wykładnik i mantysę oraz obsłużyć nieskończoności i zera.

 */

cubef:
	# r11 to znak
        movq (sgn), %r8
        movq %rdi, %r11
        andq %r8, %r11

        # r10 to wykladnik
        movq (exp), %r8
        movq %rdi, %r10
        andq %r8, %r10
	shrq $23, %r10
        leaq (%r10, %r10, 2), %r10
        sbb  $254, %r10


        # rdi to mantysa
        andq (mantysa), %rdi
        add  $0x00800000, %rdi


        # mantysa do szescianu to rsi
        movq %rdi, %rax
        mul %rdi
        mul %rdi
        movq %rax, %rsi


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
        shlq $1, %rax
        neg  %rax
        movq $0, %rax
        adc  %rax, %rax

        # zaokrąglenie to rax -- (R and S) or (R and G) <=> (G or S) and R
        orq  %r8, %rax
        andq %r9, %rax
        

        # scalanie rdx z rsi
        andq (merge), %rsi
        orq  %rdx, %rsi
        rorq $5, %rsi
        rorq %cl, %rsi
        shrq $41, %rsi
        
        

        
        # zaokrąglanie
        addq %rax, %rsi # rsi jest teraz mantysą
        andq (mantysa), %rsi

       
        addq %rcx, %r10 # inc exp

         # wynik normalny
        movq %r10, %r9
        shlq $23, %r9
        movq %rsi, %rax
        orq %r9, %rax

        # nieskończoności i zera
        test %r10, %r10
        cmovs (zero), %r10
        cmovs (zero), %rax
	
        movq $0xFF, %r9
        cmp  %r10, %r9
        cmovle (exp), %rax

        orq %r11, %rax
        ret

        
        .size   cubef, .-cubef
