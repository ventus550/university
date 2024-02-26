	.text
	.globl	bitrev
	.type	bitrev, @function


bitrev:
	# r11 to znak
        movq $0x80000000, %r8
        movq %rdi, %r11
        andq %r8, %r11

        # r10 to wykladnik
        movq $0x7F800000, %r8
        movq %rdi, %r10
        andq %r8, %r10
		shrq $23, %r10
        leaq (%r10, %r10, 2), %r10
        sbb  $254, %r10

		



        # rdi to mantysa
        movq $0x007FFFFF, %r8
        andq %r8, %rdi
        add  $0x00800000, %rdi


        # mantysa do szescianu
        movq %rdi, %rax
        mul %rdi
        mul %rdi
        movq %rax, %rdi # ?


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

        # poprawka wykładnika (r10)
        addq %rcx, %r10
		
		# If negative
		test %r10, %r10
        JS  .R0

		# If infinity
        movq %r10, %r9
        movq $0xFF, %r8
		
        andq %r8, %r10
        cmp  %r10, %r9
        JNE  .RInf
		
		movq $0xFF, %r9
		cmp  %r10, %r9
        JE  .RInf

        shlq $23, %r10

        # finalna reprezentacja
        movq %rdi, %rax
        orq %r11, %rax
        orq %r10, %rax
        ret

.R0:    movq $0x00000000, %rax
        orq  %r11, %rax
		ret

.RInf:  movq $0x7F800000, %rax
        orq  %r11, %rax
		ret

	.size	bitrev, .-bitrev