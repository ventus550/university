	.file	"test1.c"
	.text
	.p2align 4
	.globl	bitcount
	.type	bitcount, @function
bitcount:
.LFB27:
	.cfi_startproc
	endbr64
	movabsq	$6148914691236517205, %rdx
	movq	%rdi, %rax
	shrq	%rax
	andq	%rdx, %rax
	movabsq	$3689348814741910323, %rdx
	subq	%rax, %rdi
	movq	%rdi, %rax
	shrq	$2, %rdi
	andq	%rdx, %rax
	andq	%rdx, %rdi
	addq	%rax, %rdi
	movq	%rdi, %rax
	shrq	$4, %rax
	addq	%rdi, %rax
	movabsq	$1085102592571150095, %rdi
	andq	%rdi, %rax
	movabsq	$72340172838076673, %rdi
	imulq	%rdi, %rax
	shrq	$56, %rax
	ret
	.cfi_endproc
.LFE27:
	.size	bitcount, .-bitcount
	.p2align 4
	.globl	clz
	.type	clz, @function
clz:
.LFB28:
	.cfi_startproc
	endbr64
	movabsq	$6148914691236517205, %rcx
	movq	%rdi, %rax
	shrq	%rax
	orq	%rax, %rdi
	movq	%rdi, %rax
	shrq	$2, %rax
	orq	%rdi, %rax
	movq	%rax, %rdi
	shrq	$4, %rdi
	orq	%rdi, %rax
	movq	%rax, %rdi
	shrq	$8, %rdi
	orq	%rax, %rdi
	movq	%rdi, %rax
	shrq	$16, %rax
	orq	%rax, %rdi
	movq	%rdi, %rax
	shrq	$32, %rax
	orq	%rdi, %rax
	notq	%rax
	movq	%rax, %rdx
	shrq	%rdx
	andq	%rcx, %rdx
	movabsq	$3689348814741910323, %rcx
	subq	%rdx, %rax
	movq	%rax, %rdx
	shrq	$2, %rax
	andq	%rcx, %rax
	andq	%rcx, %rdx
	addq	%rax, %rdx
	movq	%rdx, %rax
	shrq	$4, %rax
	addq	%rdx, %rax
	movabsq	$1085102592571150095, %rdx
	andq	%rdx, %rax
	movabsq	$72340172838076673, %rdx
	imulq	%rdx, %rax
	shrq	$56, %rax
	ret
	.cfi_endproc
.LFE28:
	.size	clz, .-clz
	.p2align 4
	.globl	solve
	.type	solve, @function
solve:
.LFB29:
	.cfi_startproc
	endbr64

	# Wypełnianie luk
	movq	%rdi, %rax
	shrq	%rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$2, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$4, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$8, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$16, %rdi
	orq		%rdi, %rax

	movq	%rax, %rdi
	shrq	$32, %rdi
	orq		%rdi, %rax

	notq	%rax

	# Popcount
	movq    $6148914691236517205, %rcx
	movq	%rax, %rdi
	shrq	%rdi
	andq	%rcx, %rdi
	subq	%rdi, %rax

	movq    $3689348814741910323, %rcx
	movq	%rax, %rdi
	shrq	$2, %rdi
	andq	%rcx, %rdi
	andq	%rcx, %rax
	addq	%rdi, %rax

	movq    $1085102592571150095, %rcx
	movq	%rax, %rdi
	shrq	$4, %rdi
	addq	%rdi, %rax
	andq	%rcx, %rax

	movq    $72340172838076673, %rcx
	imulq	%rcx, %rax
	shrq	$56, %rax
	
	ret
	.cfi_endproc
.LFE29:
	.size	solve, .-solve
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"solve: %d\n"
	.section	.text.startup,"ax",@progbits
	.p2align 4
	.globl	main
	.type	main, @function
main:
.LFB30:
	.cfi_startproc
	endbr64
	subq	$8, %rsp
	.cfi_def_cfa_offset 16
	movl	$9, %edx
	movl	$1, %edi
	xorl	%eax, %eax
	leaq	.LC0(%rip), %rsi
	call	__printf_chk@PLT
	xorl	%eax, %eax
	addq	$8, %rsp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE30:
	.size	main, .-main
	.globl	h01
	.section	.rodata
	.align 8
	.type	h01, @object
	.size	h01, 8
h01:
	.quad	72340172838076673
	.globl	m32
	.align 8
	.type	m32, @object
	.size	m32, 8
m32:
	.quad	4294967295
	.globl	m16
	.align 8
	.type	m16, @object
	.size	m16, 8
m16:
	.quad	281470681808895
	.globl	m8
	.align 8
	.type	m8, @object
	.size	m8, 8
m8:
	.quad	71777214294589695
	.globl	m4
	.align 8
	.type	m4, @object
	.size	m4, 8
m4:
	.quad	1085102592571150095
	.globl	m2
	.align 8
	.type	m2, @object
	.size	m2, 8
m2:
	.quad	3689348814741910323
	.globl	m1
	.align 8
	.type	m1, @object
	.size	m1, 8
m1:
	.quad	6148914691236517205
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
