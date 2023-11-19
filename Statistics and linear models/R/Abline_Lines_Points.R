#LOW-LEVEL FUNCTIONS(adding new objects to the graph):                           

color=colors()

#(1)

#abline()  adds a straight line to a plot;        

abline(a, b, h, v, coef,...)

#main arguments:

# a,b - if a and(or) b are defined then the straight line y=a+bx is drawn

# h - if h is defined then the straight line y=h is drawn

# v - if v is defined then the straight line x=v is drawn

#coef - numeric vector - a coefficient vector c(a,b)

#Example:

x=seq(-pi,pi,by=0.01)
y=cos(x)
plot(x,y, type="n",xlab="x", ylab="y", xlim=c(-pi-0.1,pi+0.1), ylim=c(-1.1,1.1))
abline(a=0,b=1,lty=1, col=2)
abline(a=0,b=-1,lty=2)
abline(coef=c(0,0.5),lty=3,col=4)
abline(v = -3:3, col=colors()[451:457])
abline(h=seq(-1,1,by=0.5), col=colors()[21:25])
abline(h=0,v=0,lwd=2,col="black")


#(2) 

#lines() adds line connecting the given points to a plot;                     

lines(x, y = NULL, type = "l", ...)

#main arguments:

# x - the only function argument the argument x. It can be set in the following types
#        a two components list (points coordinates)
#        matrix with two columns (first column — x-coordinate, the second column y-coordinate).
#        if x is a numeric vector (x-coordinates), then the argument y (y-coordinates) must be set.

#Example:

x=seq(-pi,pi,by=0.01) 
y=sqrt(abs(cos(x)))
y1=-sqrt(abs(cos(x))) +1

par(mfrow=c(2,1))
par(mar=rep(2,4))
plot(x,y1, type="l",xlab="x", ylab="y", xlim=c(-pi-0.1,pi+0.1), ylim=c(-0.1,1.1))
lines(x,y,col="blue",lwd=2) 
lines(x,y1,type="h",col="purple") 
lines(x,y,type="h",col="green") 
plot(x,y, type="l",xlab="x", ylab="y", xlim=c(-pi-0.1,pi+0.1), ylim=c(-0.1,1.1))
lines(x,y1,col="blue",lwd=2) 
lines(x,y,type="h",col="purple") 
lines(x,y1,type="h",col="green") 
par(mfrow=c(1,1))


#(3) 

#points() add points to a plot;                     

points(x, y = NULL, type = "l", ...)

#main arguments:

# x - the only function argument the argument x. It can be set in the following types
#        a two components list (points coordinates)
#        matrix with two columns (first column — x-coordinate, the second column y-coordinate).
#        if x is a numeric vector (x-coordinates), then the argument y (y-coordinates) must be set.

#Example:

#Let us output all characters for the points()

x=0:15
y=0:15
plot(x,y,type="n")
for (i in 0:14)  points(x[i+1],y[15],pch=i,cex = 2)
for (i in 15:25)  points(x[i+1-12],y[13],pch=i,cex = 2,col=i,bg=i)
for (i in 32:51) points(x[i+1-32],y[10],pch=i,cex = 2)
for (i in 52:71)  points(x[i+1-52],y[8],pch=i,cex = 2)
for (i in 72:91)  points(x[i+1-72],y[5],pch=i,cex = 2)
for (i in 92:111)  points(x[i+1-92],y[3],pch=i,cex = 2)
for (i in 112:127)  points(x[i+1-112],y[1],pch=i,cex = 2)


