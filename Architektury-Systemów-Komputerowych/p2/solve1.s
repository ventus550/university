	.file	"solve1.c"
	.text
	.p2align 4
	.globl	Solve
	.type	Solve, @function
Solve:
.LFB27:
	.cfi_startproc
	endbr64
	movabsq	$-71777214294589696, %rcx
	movq	%rdi, %r8
	movq	%rsi, %rdx
	movq	%rsi, %rax
	andq	%rcx, %r8
	andq	%rcx, %rdx
	xorq	%rdi, %rsi
	addq	%r8, %rdx
	movq	%rdi, %r8
	notq	%rsi
	andq	%rcx, %rdx
	movabsq	$71777214294589695, %rcx
	andq	%rcx, %r8
	andq	%rcx, %rax
	addq	%r8, %rax
	andq	%rcx, %rax
	movq	%rdx, %rcx
	orq	%rax, %rcx
	movq	%rdi, %rax
	shrq	$7, %rdi
	xorq	%rcx, %rax
	andq	%rax, %rsi
	movabsq	$-9187201950435737472, %rax
	andq	%rax, %rsi
	movabsq	$72340172838076673, %rax
	andq	%rax, %rdi
	leaq	(%rsi,%rsi), %rdx
	shrq	$7, %rsi
	movabsq	$9187201950435737471, %rax
	subq	%rsi, %rdx
	addq	%rdi, %rax
	andq	%rdx, %rax
	notq	%rdx
	andq	%rcx, %rdx
	leaq	(%rax,%rdx), %rax
	ret
	.cfi_endproc
.LFE27:
	.size	Solve, .-Solve
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Solve: %lX\n"
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
	movabsq	$47851836970893439, %rdx
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
