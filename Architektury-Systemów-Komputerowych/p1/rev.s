
	.text
	.globl	rev
	.type	rev, @function

rev:
		rolw $8, %di
		roll $16, %edi
		rolw $8, %di
		movq %rdi, %rax
		movq $0xF0F0F0F0F0F0F0F0, %r8
		

	ret

	.size	rev, .-rev