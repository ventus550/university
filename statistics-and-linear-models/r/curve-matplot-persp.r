#High-level functions (general):                           

color=colors()

#(1)

#curve()} creates a plot of a function over certain interval

curve(expr, from = NULL, to = NULL, n = 101, add = FALSE, type  =  "l",  ...)

#main arguments:

# expr - expression as a function of x or the name of the function to plot

#from and to - numeric arguments-boundaries of the segment where the graph is drawn. 
#              If these parameters are omitted, the boundaries are defined by the values of the x  
#              If x is not defined, then the graph is plotted on the segment [0; 1].

#n - numeric argument - the number of points where the expr value is defined.

#add - logical argument - whether to add a curve to an existing plot (add=TRUE) 
#              or to create a new graphic window (add=FALSE).

#Example:

#Let f_1(x)=x^3-3x
#    f_2(x)=x^2-2
#    f_3(x)=cos(x)
#    f_4(x)=sin(cos(x))exp(-x/2)

#The graphs of this functions is created: f_1 and f_2 on the plot1, f_3 on the plot 2
# f_3 is created on the plot 3 (using curve()) and on the plot 4 (using plot())  to compare the results

par(mfrow=c(2,2))
curve(x^3-3*x, -2, 2)
curve(x^2-2, add = TRUE, col = "violet")
plot(cos, -pi, 3*pi)
plot(cos, xlim = c(-pi,3*pi), n = 1001, col = "blue", add=TRUE)
f1 <- function(x) sin(cos(x)*exp(-x/2))
curve(f1, -8, 7, n=2001)
plot (f1, -8, -5)
par(mfrow=c(1,1))


#(2)

#matplot() - creates plot for matrix columns

matplot(x, y, type = "p",...)

#main arguments:


#x,y - vectors or matrices of data

#Example:

matplot(iris[,1:4],type = 'o', pch = 20)

#(3)

#persp() creates 3D plots

# persp () does not work directly with the function z=f(x,y), 
# but with the matrix of the function's values z_ij =f(x_i,y_j) in the grid nodes. 
#To calculate the z values, it is convenient to use the outer() function

persp(x, y, z,
      theta = 0, phi = 15, r = sqrt(3), d = 1,
      scale = TRUE, expand = 1)

#Main arguments:

#x,y - numeric vectors - locations of grid lines at which the values in z are measured (in ascending order)

#z - numeric matrix - values to be plotted

#theta, phi  - azimuthal direction and colatitude -  angles defining the viewing direction

#r,d, expand - parameters parameters for tuning 3d images

#Example:

x<-(1:50)/10
y<-(20:70)/10
f<-function(x,y){sin(x)^2+cos(y)^2}
z<-outer(x,y,f)
persp(x,y,z,theta=30,phi=30, expand=.5, col="lightblue")


