	.file	"test.c"
	.text
	.p2align 4
	.globl	reverse
	.type	reverse, @function
reverse:
.LFB27:
	.cfi_startproc
	endbr64
	movabsq	$1085102592571150095, %rdx
	movq	%rdi, %rax
	movabsq	$6148914691236517205, %rcx
	bswap	%rax
	movq	%rax, %rdi
	salq	$4, %rax
	shrq	$4, %rdi
	andq	%rdx, %rdi
	movabsq	$-1085102592571150096, %rdx
	andq	%rdx, %rax
	orq	%rax, %rdi
	movabsq	$3689348814741910323, %rax
	movq	%rdi, %rdx
	salq	$2, %rdi
	shrq	$2, %rdx
	andq	%rax, %rdx
	movabsq	$-3689348814741910324, %rax
	andq	%rax, %rdi
	orq	%rdi, %rdx
	movq	%rdx, %rax
	addq	%rdx, %rdx
	shrq	%rax
	andq	%rcx, %rax
	movabsq	$-6148914691236517206, %rcx
	andq	%rcx, %rdx
	orq	%rdx, %rax
	ret
	.cfi_endproc
.LFE27:
	.size	reverse, .-reverse
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"%lX\n"
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
	leaq	.LC0(%rip), %rsi
	movl	$1, %edi
	xorl	%eax, %eax
	movabsq	$-5208459330143660587, %rdx
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
