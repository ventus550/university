# PROGRAMMING IN R

# FUNCTIONS

# (a) functions are objects in R like vectors, matrices, frames etc

# (b) to create new function you should create new object of type function and assign it with a variable

variable=function(formal parameters of function) {a sequence of commands}

# (c) the command 
 return (value) 
# returns the result of the function or (if the command return() is absent) the result of the last command

#Example:

t.sum=function(x,t){sum(x[x>t])}         #the function t.sum summize elements of the vector x that greater than level t

t.sum(1:100,50)                          #calling the function t.sum
t.sum(t=50, 1:100)                       #you can call the function changing the order of parameters

t.sum=function(x,t=0){sum(x[x>t])}       #you can set the default parameter value

t.sum(-100:100)                          #you don't need to define the value of the second parameter; by default,it is equal to 0

t.sum=function(x,t=sum(x)/length(x)){sum(x[x>t])} #value of a parameter by default could be an expression of other formal parameters.
                                                  #if the value of t does not defined the functiom t.sum summize elements of the vector 
                                                  #x that greater than mean of the elements of x
t.sum(0:100)

#(d) local and global variables

z=42
t.sum=function(x,t=0){                    # there could be several commands in the function. Here z is local variable,
  z=x>t; sum(x[z])}                       # it exists only in the function. If you have another variable with the same name
                                          # outside the function, its value does not change after calling the function
t.sum(-100:100)
z

n=1
t.sum=function(x,t=0){                    # if you need to change a global variable in the function, you should do  
  z=x>t; sum(x[z]); n<<-n+1}              # global assighnment in the function: <<-
t.sum(0:100)                              # here n shows how many times the function t.sum was called
n

#CONDITIONAL EXECUTION IF

#There are 3 versions of coditional structures:

if(condition){a sequence of commands}

if(condition){a sequence of commands - 1} else {a sequence of commands - 2} #a sequence of commands - 1 executes when condition is true, 
                                                                            #a sequence of commands - 2 executes when condition is false, 

ifelse(condition,command 1, command 2 )  #command - 1 executes when condition is true, 
                                         #command - 2 executes when condition is false,

#Example

sgn=function(x){if(x>0) return(1) else {if (x==0) return(0) else return(-1)}}
sgn(0)
sgn(-5)

sgn1=function(x){ifelse((x>0), return(1),ifelse((x==0), return(0), return(-1)))}
sgn1(0)
sgn1(-5)



#FOR LOOP

for (variable in vector) {a sequence of commands}

#example

vect_diff=function(x){                         #for given vector x=(x_1,x_2, ... , x_n) this function 
  n=length(x)-1;  z=c() ;                      #calculate vector z=(x_2-x_1, ... , x_n-x_{n-1})
  for (i in 1:n) {z=c(z,x[i+1]-x[i])};         #and prints this vectors on the screen
  print(x); print(z)
}

vect_diff((1:20)^2)


#WHILE LOOP

while(condition) {a sequence of commands} #a sequence of commands executes while the condition is true

#example

xcosx_while=function(eps){                           #this function solves the equation x=cos(x) with precision eps using  
  z=0;n=0;                                     #method of successive approximations. the function calculates the number
  while(abs(z-cos(z))>eps){z=cos(z); n=n+1};   #of iterations required to achieve the specified precision
  print(n)
}

xcosx_while(0.0000001)

#REPEAT LOOP

repeat({a sequence of commands, it should include command break() })

#this loop is useful in the case when you need to check the break condition at the end or in the middle of the 
# loop. 
# also you can use command 
next()
#that halts the processing of the current iteration and starts next itteration from the first command.

#commands 
break() and next()
#can be used in while and for loop also


#example

xcosx_repeat=function(eps){                    #this function solves the equation x=cos(x) with precision eps using  
  z=0;n=0;                                     #method of successive approximations. the function calculates the number
  repeat({z=cos(z); n=n+1;                     #of iterations required to achieve the specified precision
  if(abs(z-cos(z))<eps) break});   
  print(n)
}

xcosx_repeat(0.0000001)

#Example

F=datasets::iris
F
names=c("mean","median","variance")

result=function(x,n=2){
  y=round(c(mean(x),median(x),var(x)),n);
  return(y)
}

F1=apply(iris[,1:4],2,result)
row.names(F1)=names
F1

n=length(levels(iris$Species))
F2=c()

for (i in 1:n) {
  F2=rbind(F2,apply(iris[iris$Species==levels(iris$Species)[i],1:4],2,result))
}
F2=as.data.frame(F2)

F2=cbind(rep(levels(iris$Species),each=3),rep(names,3),F2)
F2
colnames(F2)[1:2]=c("Species","Characteristic")
F2

