	.file	"test.c"
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
	.section	.rodata
	.align 16
	.type	baz, @object
	.size	baz, 24
baz:
	.ascii	"abc"
	.zero	1
	.long	42
	.quad	-3
	.long	1068827777
	.zero	4
	.comm	array,800,32
	.ident	"GCC: (Ubuntu 9.3.0-10ubuntu2) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
