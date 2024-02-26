	.file	"test.c"
	.text
	.globl	endian
	.def	endian;	.scl	2;	.type	32;	.endef
	.seh_proc	endian
endian:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$16, %rsp
	.seh_stackalloc	16
	.seh_endprologue
	roll	$16, -4(%rbp)
	movl	-4(%rbp), %eax
	shrl	$8, %eax
	andl	$16711935, %eax
	movl	%eax, %edx
	movl	-4(%rbp), %eax
	sall	$8, %eax
	andl	$-16711936, %eax
	orl	%edx, %eax
	movl	%eax, -4(%rbp)
	nop
	addq	$16, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.def	__main;	.scl	2;	.type	32;	.endef
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	call	__main
	call	endian
	movl	$0, %eax
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (x86_64-posix-seh-rev0, Built by MinGW-W64 project) 8.1.0"
