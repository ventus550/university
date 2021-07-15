	.file	"test1.c"
	.text
	.globl	m1
	.section	.rodata
	.align 8
	.type	m1, @object
	.size	m1, 8
m1:
	.quad	6148914691236517205
	.globl	m2
	.align 8
	.type	m2, @object
	.size	m2, 8
m2:
	.quad	3689348814741910323
	.globl	m4
	.align 8
	.type	m4, @object
	.size	m4, 8
m4:
	.quad	1085102592571150095
	.globl	m8
	.align 8
	.type	m8, @object
	.size	m8, 8
m8:
	.quad	71777214294589695
	.globl	m16
	.align 8
	.type	m16, @object
	.size	m16, 8
m16:
	.quad	281470681808895
	.globl	m32
	.align 8
	.type	m32, @object
	.size	m32, 8
m32:
	.quad	4294967295
	.globl	h01
	.align 8
	.type	h01, @object
	.size	h01, 8
h01:
	.quad	72340172838076673
	.globl	min
	.align 8
	.type	min, @object
	.size	min, 8
min:
	.quad	3472884
	.text
	.globl	bitcount
	.type	bitcount, @function
bitcount:
.LFB0:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	%rax
	movq	%rax, %rdx
	movabsq	$6148914691236517205, %rax
	andq	%rdx, %rax
	subq	%rax, -8(%rbp)
	movabsq	$3689348814741910323, %rax
	andq	-8(%rbp), %rax
	movq	-8(%rbp), %rdx
	movq	%rdx, %rcx
	shrq	$2, %rcx
	movabsq	$3689348814741910323, %rdx
	andq	%rcx, %rdx
	addq	%rdx, %rax
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$4, %rax
	movq	%rax, %rdx
	movq	-8(%rbp), %rax
	addq	%rax, %rdx
	movabsq	$1085102592571150095, %rax
	andq	%rdx, %rax
	movq	%rax, -8(%rbp)
	movabsq	$72340172838076673, %rax
	imulq	-8(%rbp), %rax
	shrq	$56, %rax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	bitcount, .-bitcount
	.globl	clz
	.type	clz, @function
clz:
.LFB1:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$8, %rsp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	%rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$2, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$4, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$8, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$16, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$32, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	notq	%rax
	movq	%rax, %rdi
	call	bitcount
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	clz, .-clz
	.globl	solve
	.type	solve, @function
solve:
.LFB2:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	%rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$2, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$4, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$8, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$16, %rax
	orq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$32, %rax
	orq	%rax, -8(%rbp)
	notq	-8(%rbp)
	movq	-8(%rbp), %rax
	shrq	%rax
	movq	%rax, %rdx
	movabsq	$6148914691236517205, %rax
	andq	%rdx, %rax
	subq	%rax, -8(%rbp)
	movabsq	$3689348814741910323, %rax
	andq	-8(%rbp), %rax
	movq	-8(%rbp), %rdx
	movq	%rdx, %rcx
	shrq	$2, %rcx
	movabsq	$3689348814741910323, %rdx
	andq	%rcx, %rdx
	addq	%rdx, %rax
	movq	%rax, -8(%rbp)
	movq	-8(%rbp), %rax
	shrq	$4, %rax
	movq	%rax, %rdx
	movq	-8(%rbp), %rax
	addq	%rax, %rdx
	movabsq	$1085102592571150095, %rax
	andq	%rdx, %rax
	movq	%rax, -8(%rbp)
	movabsq	$72340172838076673, %rax
	imulq	-8(%rbp), %rax
	shrq	$56, %rax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	solve, .-solve
	.section	.rodata
.LC0:
	.string	"solve: %d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB3:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movabsq	$31525197391593472, %rdi
	call	solve
	movl	%eax, %esi
	leaq	.LC0(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
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
