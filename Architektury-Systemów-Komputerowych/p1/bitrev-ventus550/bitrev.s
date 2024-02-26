
	.text
	.globl	bitrev
	.type	bitrev, @function


bitrev:
		movq $0xF0F0F0F0F0F0F0F0, %r8
		movq $0x3333333333333333, %r9
		movq $0xAAAAAAAAAAAAAAAA, %r10
        movq %rdi, %rax
		
		rolw $8, %di
		roll $16, %edi
		rolw $8, %di
		
		rorq $32, %rax	
		rolw $8, %ax
		roll $16, %eax
		rolw $8, %ax

		salq $32, %rdi
		addq %rdi, %rax

        movq %rax, %rdi
        andq %r8, %rdi
        shrq $4, %rdi
        shlq $4, %rax
        andq %r8, %rax
        addq  %rdi, %rax

        movq %rax, %rdi
        andq %r9, %rdi
		shlq $2, %rdi
		shrq $2, %rax
        andq %r9, %rax
        addq  %rdi, %rax

        movq %rax, %rdi
        andq %r10, %rdi
        shrq $1, %rdi
        shlq $1, %rax
        andq %r10, %rax
        addq  %rdi, %rax

	ret

	.size	bitrev, .-bitrev