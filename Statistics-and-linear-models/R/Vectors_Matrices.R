#Start of work. Main data types: vectors and matrices


#Help:

?sin            #get help on the command 'sin' from installed packages;
??sin           #gets help on the command 'sin' from all packages;
example('rep')  #gets examples of using the command 'rep'.


#Main concepts:

# 1)R consists of commands:

1+1              # the expression;
x<-1+1           # the assighnment

#or 

x=1              #the assighnment;


# 2) Commands work with objects: vectors, matrices, frames, functions, etc;


#TYPES OF DATA

#VECTORS

#Types of vectors:

# 1) logical (consists of values 'T' = True or 'F' = False);
# 2) integer (consists of integer numbers);
# 3) numeric (consists of real numbers);
# 4) complex (consists of complex numbers);
# 5) character (consists of symbols or strings).

#How to create a vector (simple examples):

c(1,2,3,4)
x<-c(1,2,3,4)
y<-c('a','b','ab')

#Note that: Numbers are vectors of length 1!
  
#Operations:

#logical: 

# & -- and;
# | -- or;
# ! -- rejection;
# >, <, >=, <=  -- comparison;
# == -- logical equality;
#!=  -- logical inequality

#Example:

2==3

#arithmetical: 

#+, -, *, / , ^ (power), %/% (integer division), %% (reminder of division)
#round(x,n) (round a number x till n decimal places)

#Examples:

2+3
2-3
2*3
2/3
2^3
15%/%6
15%%6
round(1.23456,3)
x<-c(1,2,3,4)
x+3               #adds 3 to each element of x;
x*x               #if x=(x_1,x_2,x_3,x_4) then x*x=(x_1*x_1,x_2*x_2,x_3*x_3,x_4*x_4)
z<-c(-3,4)
x+z               #replicates z till the length of x and adds them elementwise
l<-x>z            #l is the vector of logical type
x+l               #when you add vector of logical type to numerical, R assume that True=1, False=0
1/0               #as the result you will obtain the in-build constant 'Inf' 

#functions: 

#sqrt() -- square root, 
#abs()  -- absolute value,
#sin(), cos(), tan() -- trigonometric functions
#exp()  -- exponent
#log(), log10(), log(base = ) - logarithms

#functions and operations are applied elementwise!

#Examples:

x<-c(1,2,3,4)

exp(x)
sqrt(x)


#Convenient ways to create a vector:

# 1) seq(from,to,by) -- creates a vector whose elements form an arithmetic progression from the number 
#                       'from' till the number 'to' with the step 'by';

#Example:

seq(1.005,2,0.005)

# 2) if you need to create an arithmetic progression with step 1 or -1, you can do it using the symbol ":"

#Examples:
1:100             #1,2,3,...,100
(-5):(-10)        #-5,-6,...,-10
-(5:10)           #the same result as in previuos example
(-5):10           #-5,-4,...,10

x<-1:100
x+2:3             #adds to the x=(1,2,3,...,100) vector (2,3,2,3,...,2,3)
x+2:4             #there is an error here because length x is not divisible by length 2:4;


# 3) the union of vectors:

#Examples:

x1<-c(x,z)        #creates new vector that is the union of the vectors x and z;
x2<-c(z,5:20)     #creates new vector that is the union of the vectors z and 5:20;  

# 4)  replication

#Examples:

rep(1:5,5)          #creates the vector, in which  1:5 is replicated 5 times;
rep(1:5,length=42)  #replicates 1:5 till the length 42 is reached
rep(1:5, each=5)   #replicates '1' 5 times, then '2' 5 times and so on 


#Vector's indexation -- how to call elements of a vector

#x[]  -- in square brackets there can be 
#any vector (numbers of vector's elements) 
#logical condition on elements of vector

#the numeration of vector's elements starts from 1

#Examples:

x=100:1

x[2]            #element of x that stands on the place 2
x[-2]           #all elements of x except the second
x[2:10]         #elements of x that stands on the places 2:10
x[-2:10]        # there is error because -2:10 is the sequence -2,-1,...,10 but a vector cannot have nonpositive indexes
x[-(2:10)]      #all elements of x except the 2:10
x[seq(1,50,3)]  #elements of x that stands on the places 1,4,7,..,49

y=letters       #'letters' is in-build vector of character type consists of latin letters in alphabet order
y[12:5]         # elements of x that stands on the places 12:5
y[c(2,5)]       # elements of x that stands on the places 2 and 5

x[x<=5]         # elements of x that satisfies the condition x<=5
x[x<=5|x>90]    # elements of x that satisfies the condition (x<=5) or (x>90)


#MATRICES

#matrices consists of the one type of elements!!!

#How to create a matrix

#a) from a vectors using command

#rbind() that combines vectors by rows
#cbind() that combines vectors by columns

#Examples:

x1<-1:10
x2<-11:20

z1<-rbind(x1,x2)
z1
z2<-cbind(x1,x2)
z2

#b) from a vector using command

# matrix()  that transforms vector to matrix

#matrix(x, nrow=m, ncol=n )  -- transforms vector x to matrix of dimension mxn

#Examples:

x<-1:100

matrix(x,nrow = 5, ncol = 20)   #transforms vector x to the matrix of dimension 5x20
matrix(x,nrow = 5,ncol = 5)    #transforms 25 elements of vector x to the matrix of dimension 5x5
matrix(x,nrow = 10, ncol = 20)  #transforms vector x to the matrix of dimension 10x20. It replicates elemnents ox x twice
matrix(x, nrow = 5, ncol = 20, byrow = T) #transforms vector x to the matrix of dimension 5x20, 
                                          #the matrix is fiiled by elements of x by rows (by default - by columns)

#c) from a vector using command

#dim() that transforms the dimension of the object

#Examples:

dim(x)<-c(5,20)          #the dimension of vector x transforms from 1x100 to 5x20


#d) diagonal matrix

#Examples:

diag(8)                  #creates the identical matrix of dimension 8x8
diag(x[50:59])           #creates the diagonal matrix with elements x[50:59] on diagonal.
diag(x)<-0               #diagonal elements of x are changed to 0
x

#Matrix's indexation -- how to call elements of a matrix

#The same idea as for vectors, but there are 2 indexes separated by a comma. 
#The first index is a condition for the row number, the second index is for the column number

#Examples:

x[2,3]                  #element that stands at the intersection of 2 row and 3 column of the matrix x
x[2,]                   #elements of the 2  row of the matrix x
x[,3]                   #elements of the 3  column of the matrix x
x[1:2,5:10]             #elements that stands at the intersection of 1:2 rows and 5:10 columns of the matrix x


#Operations and functions with matrices

#functions and operations (similar as for vectors) are applied elementwise!

#Examples:

x+x                     # sum
x*x                     # elementwise product
sin(x)                  # sin is applied elementwise

#%*%   -- matrix product
#t()   -- matrix transpositon

t(x)                    #the matrix transposed to x
x%*%t(x)                #x*t(x) (matrix product)
t(x)%*%x                #t(x)*x (matrix product)

#solve(A,B)  -- solves the system of linear equations Ax=B, when B is a vector
#               or matrix equation when B is a matrix:
#               X=A^{-1}B  on the assumption that A is nondegenerate (det A!= 0)

A=matrix(c(2,1,3,0,-1,2,2,-4,1),nrow = 3,ncol = 3)
B=c(1,2,3)
det(A)
solve(A,B)

#some useful functions (can be applied as for vectors as for matrices)

#length()                  -- calculates the lengh of a vector/ matrix;
#max(), min()              -- calculates the maximal/minimal element of a vector/matrix;
#which.max(), which.min()  -- determines the index of the (first) minimum or maximum element of a vector/matrix;
#sum()                     -- summizes elements of a vector/matrix;  
#prod()                    -- calculates the product of elements of a vector/ matrix;
#sort()                    -- sorts elements of a vector/ matrix;
#sort(, decreasing =T)     -- sorts elements of a vector/ matrix in the descending order
#apply(matrix, 1 , FUN)    -- applies a function FUN to each row of the matrix
#apply(matrix, 2 , FUN)    -- applies a function FUN to each column of the matrix

#Examples:

length(x)
max(x)
which.max(x)
sum(x)
sort(x)
apply(x,1,sum)
apply(x,2,min)


