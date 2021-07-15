#include <alloca.h>
#include <iso646.h>

	long aframe(long n, long idx, long *q) {
	long i;
	long **p = alloca(n * sizeof(long *));
	p[n-1] = &i;
	for (i = 0; i < n; i++)
	p[i] = q;
	return *p[idx];
}	

//gcc -Og -fomit-frame-pointer -fno-stack-protector alloha.c -o aloha
int main() <%
	int xd<:0:><:0:>;	
	return 2 bitor not 2;
%>
