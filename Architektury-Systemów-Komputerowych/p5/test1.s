	.file	"test1.c"
	.text
	.p2align 4
	.globl	solve
	.type	solve, @function
solve:
.LFB27:
	.cfi_startproc
	endbr64
	movq	%rdi, %rax
	movabsq	$1085102592571150095, %rdi
	movq	%rax, %rdx
	shrq	$4, %rax
	andq	%rdi, %rdx
	andq	%rdi, %rax
	movq	%rdx, %rcx
	shrq	$8, %rcx
	addq	%rcx, %rdx
	movq	%rax, %rcx
	shrq	$8, %rcx
	addq	%rcx, %rax
	movq	%rdx, %rcx
	shrq	$16, %rcx
	addq	%rdx, %rcx
	movq	%rax, %rdx
	shrq	$16, %rdx
	addq	%rdx, %rax
	movq	%rcx, %rdx
	shrq	$32, %rdx
	addq	%rcx, %rdx
	subq	%rax, %rdx
	shrq	$32, %rax
	subq	%rax, %rdx
	movq	%rdx, %rax
	shrq	$4, %rdx
	andl	$15, %edx
	andl	$15, %eax
	subq	%rdx, %rax
	leaq	17(%rax), %rdx
	cmpq	$511, %rax
	cmova	%rdx, %rax
	ret
	.cfi_endproc
.LFE27:
	.size	solve, .-solve
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"solve: %d => %d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB28:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$1, %ecx
	movl	$1, %edx
	xorl	%eax, %eax
	leaq	.LC0(%rip), %rsi
	movl	$1, %edi
	call	__printf_chk@PLT
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE28:
	.size	main, .-main
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
