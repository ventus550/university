	.text
	.globl	bitrev
	.type	bitrev, @function



bitrev:
# dzielimy cyfry na parzyste i nieparzyste
	movq    %rdi, %rax
	movq 	$0x0f0f0f0f0f0f0f0f, %rsi
    andq    %rsi, %rdi # rdi to parzyste

    shrq    $4, %rax
    andq    %rsi, %rax # rax to nieparzyste


    # sumowanie

    # sumy czworek
    movq %rdi, %rsi
    shrq $8, %rsi
    addq %rsi, %rdi

    movq %rax, %rcx
    shrq $8, %rcx
    addq %rcx, %rax


    # sumy osemek
    movq %rdi, %rsi
    shrq $16, %rsi
    addq %rsi, %rdi

    movq %rax, %rcx
    shrq $16, %rcx
    addq %rcx, %rax


    # sumy szesnastek
    movq %rdi, %rsi
    shrq $32, %rsi
    addq %rsi, %rdi

    movq %rax, %rcx
    shrq $32, %rcx
    addq %rcx, %rax

    # odejmujemy nieparzyste (rax) od parzystych (rdi)
    # do tego miejsca okej!
    subq	%rax, %rdi
	cmpq	$511, %rax
	leaq	136(%rdi), %rax
	cmova	%rax, %rdi

	movq	%rdi, %rax
	shrq	$4, %rdi
	andl	$15, %edi
	andl	$15, %eax

	subq	%rdi, %rax
	leaq	17(%rax), %rdi
	cmpq	$511, %rax
	cmova	%rdi, %rax

    ret

	.size	bitrev, .-bitrev