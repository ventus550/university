	.file	"baz.c"
	.text
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
	.ident	"GCC: (Ubuntu 9.3.0-10ubuntu2) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
