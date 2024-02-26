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
        .globl  addsb
        .type   addsb, @function

/*
 * W moim rozwiązaniu używam następującej techniki: 
        Zaczynam od podzielenia wektorów wejściowych X, Y na dwie części takie, że pierwsza część zawiera
        składowe o nieparzystych indeksach, a druga o indeksach parzystych np.
        X -> X1 + X2, X1 = X & 0xFF00FF00FF00FF00, X2 = X & 0x00FF00FF00FF00FF

        Powstałe "luki" między składowymi są bardzo wygodne, ponieważ teraz możemy dodawać składowe bez ryzyka
        uszkodzenia wektora w przypadku wystąpienia zjawiska przepełnienia tj. wykonujemy X1 + Y1, X2 + Y2.
        W tym kroku trzeba zadbać o użycie odpowienich masek, ale ogólnie celujemy w taką reprezentację wektora ("XY"),
        w której wszystkie składowe są wynikami dodawań składowych wektorów wejściowych X, Y po indeksach w taki sposób, że
        żadna nie jest zanieczyszczona przez wynik sąsiada.

        W kolejnym kroku budujemy maskę przepełnienia ("OM") tj. taką liczbę, w której jedynki wypełniają miejsca, w których
        nastąpiło przepełnienie, a zera miejsca pozostałe.
        Możemy takie coś zrobić korzystając z wiedzy, że przepełnienie na pewno nastąpiło jeśli znak dodanych składowych
        był jednakowy oraz znak wyniku był do niego przeciwny.
        W rozwiązaniu wykonywana jest pewna akrobatyka bitowa dzięki, której możemy "rozmazać" wynik powyższego testu (0 lub 1)
        na wszystkich bitach składowej wyniku w relatywnie kilku instrukcjach.

        Ostatecznie wystarczy już tylko przygotować wektor składowych maksymalnych i minimalnych, a następnie wstawić te wartości
        w miejsca wskazane przez maskę "OM" (pozostałe miejsca pozostają oczywiście niezmienione, tj. są nadal wynikiem dodawania).


 */

addsb:

        # Przygotowanie reprezentacji wektora wynikowego
        movq %rdi, %r8                           
        movq %rsi, %rdx                          
        movq $0xFF00FF00FF00FF00, %r10                          
        andq %r10, %r8                           # r8 = X1
        andq %r10, %rdx                          # rdx = Y1
        addq %r8, %rdx                           # rdx = X1 + Y1
        andq %r10, %rdx

        movq %rdi, %r8                           
        movq %rsi, %rax                          
        movq $0x00FF00FF00FF00FF, %r10                          
        andq %r10, %r8                           # r8 = X2
        andq %r10, %rax                          # rax = Y2
        addq %r8, %rax                           # rax = X2 + Y2
        andq %r10, %rax

        addq %rdx, %rax                          # rax := "XY"

        # Wykrywanie overflow'a
        xorq %rdi, %rsi                          # rsi := "OM"
        notq %rsi

        movq %rdi, %r10                          
        xorq %rax, %r10

        andq %r10, %rsi                          # znaki operandow sa takie same
                                                 # oraz znak sumy jest inny niż znak operandu, wtedy 1 wpp 0
        movq $0x8080808080808080, %r10
        andq %r10, %rsi

        movq %rsi, %r9
        shrq $7, %r9
        leaq (%rsi, %rsi), %rsi
        subq %r9, %rsi                           # od teraz rsi jest w pewnym sensie maską overflowa

        # min/maxy
        andq %r10, %rdi
        shrq $7, %rdi
        movq $0x7F7F7F7F7F7F7F7F, %r10
        addq %r10, %rdi                          # rdi zawiera teraz odpowiednie wartości min i max dla sum składowych wektorów

        # obliczanie wyniku
        andq %rsi, %rdi
        notq %rsi
        andq %rsi, %rax
        addq %rdi, %rax

	ret



        .size   addsb, .-addsb
