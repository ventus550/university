	.file	"foobar.c"
	.text
	.globl	foobar
	.type	foobar, @function
foobar:
	endbr64
	pushq	%rbp
	movq	%rsp, %rbp
	nop
	popq	%rbp
	ret
	.size	foobar, .-foobar
	.ident	"GCC: (Ubuntu 9.3.0-10ubuntu2) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"