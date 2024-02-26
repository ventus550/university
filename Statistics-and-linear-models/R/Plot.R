# BASIC GRAPHICS IN R

#1. The command plot() -- the main function of creating two-dimensional graphs

#Example:

x<-sin(1:20)
y<-cos(1:20)
plot(x,y)          # The plot () first creates a new window, and then outputs objects (in our case, points) to it.
                   #The result is a set of points with coordinates (x,y)

plot(x,y, asp=1)                                                     #the option asp controls y/x aspect ratio
plot(x,y, asp=1, col="red")                                          #+ red  color of points
plot(x,y, asp=1, col="red", pch=8)                                   #+ new symbol for points
plot(x,y, asp=1, col="red", pch=8, cex = 2)                          #+ greater size of points
plot(x,y, asp=1, col="red", pch=8, cex = 2, main = "Circle")         #+ title
plot(x,y, asp=1, col="red", pch=8, cex = 2, main = "Circle", xlab = "x-axis", ylab = "y-axis")   #+ captions for x- and y- axes


#two possible ways to call command plot()

# plot(x,y,...)           # set of points with coordinates (x,y)
# plot(FUN,a,b, ....)     # set of points with coordinates (x,FUN(x)), x\in[a,b]

#Example

x<-seq(-2*pi,2*pi,by=0.01)
y<-cos(x)

plot(x,y)   
plot(cos,-2*pi,2*pi)


# The structure of plot()

# plot(x,y,type=..., graphic options)
# plot(FUN,x,y, ....)    



#type=... -- determine the type of the plot

#Possible types + example

x<- (-4):4
y<- x^2

plot(x,y, type = "p")      #"p" -- points
plot(x,y, type = "l")      #"l" -- lines  
plot(x,y, type = "o")      # "o" -- for both lines and points, lines cover points
plot(x,y, type = "b")      # "o" -- for both lines and points, lines touch points
plot(x,y, type = "c")      # similar to the previous one, but without points
plot(x,y, type = "h")      # vertical segments connecting the points with x-axis
plot(x,y, type = "s")      # step lines  (at a point, first horizontal, then vertical line)
plot(x,y, type = "S")      # step lines  (at a point, first vertical, then horizontal line)
plot(x,y, type = "n")      # the coordinate plane that corresponds to all the specified points is displayed, 
                           # but the points are not displayed. This option is used to prepare the place where 
                           # future objects will be displayed by other functions

# graphic options (not all, just the most useful), 

#Titles and axes settings

# main, sub -- character type -- title and sub title for the plot 
# xlab, ylab -- character type -- title for the x- and y- axes
# xlim, ylim -- numeric vectors c(x_1,x_2), c(y_1,y_2) -- set scale limits
# font.axis, font.lab, font.main, font.sub -- 1,2,3 or 4 -- font type for axes titles, main and sub titles
#                                      1 --- normal (by default)
#                                      2 --- bold 
#                                      3 --- italic
#                                      4 --- bold and italic

# log -- is equal to "x", "y" or "xy"  -- name of the axis that is converted to the logarithmic scale
# xaxt, yaxt -- character -- remove x-axis labels (xaxt = "n") or y-axis labels (yaxt = "n") 
# asp -- number -- y/x aspect ratio
# lab -- c(x,y,len) -- the number of labels on axes (x - on the x-axis, y - on the y-axis, len - unused parameter)
# las  --- is equal to 0, 1, 2 or 3 -- how the axis labels are located w.r.t  axes:
#                                      0 --- parallel to the axes (by default)
#                                      1 --- horizontally 
#                                      2 --- perpendicular  to the axes
#                                      3 --- vertically
# col.axis -- character -- color of axes labels
# col.main, col.sub -- character -- color of title and sub title
# fg -- character - color of the border around the graph


#Image settings

# col -- character or integer -- color of objects 
# pch -- integer, positive -- symbol for points
# cex -- integer, positive -- the size of symbols
# lwd -- positive, integer -- the width of lines
# lty -- 0,1,2,3,4,5 or 6 -- the style of lines
#                                      0 --- "blank" 
#                                      1 --- "solid" (by default)
#                                      2 --- "dashed"
#                                      3 --- "dotted"
#                                      4 --- "dotdash"
#                                      5 --- "longdash"
#                                      6 --- "twodash"

#Examples of different settings of axes and titles

x<- seq((-4)*pi,4*pi,0.25)
y<- cos(x)

plot(x,y, sub = "Trigonometric functions", main =  "Cosine", xlab = "x-axis", ylab = "y-axis")

plot(x,y, sub = "Trigonometric functions", main =  "Cosine", xlab = "x-axis", ylab = "y-axis", 
     font.main=4, font.sub=2, font.lab=3,font.axis = 2)

plot(x,y, main =  "Cosine", xlab = "x-axis", ylab = "y-axis", xlim = c(-20,20), ylim = c(-5,5))

plot(x,y+2, main =  "Cosine", xlab = "x-axis", ylab = "y-axis", ylim = c(1,5), log="y")

plot(x,y,  ylim = c(-3,3), main =  "Cosine", xaxt  = "n", yaxt="n")

plot(x,y, main =  "Cosine", xlab = "x-axis", ylab = "y-axis", ylim = c(-3,3), lab = c(20,20,1))

plot(x,y, main =  "Cosine", xlab = "x-axis", ylab = "y-axis", ylim = c(-3,3),  lab = c(30,20,1), las=2)

plot(x,y, sub = "Trigonometric functions", main =  "Cosine", xlab = "x-axis", ylab = "y-axis", col.axis="blue", fg="red")

plot(x,y, sub = "Trigonometric functions", main =  "Cosine", xlab = "x-axis", ylab = "y-axis", col.axis="blue", fg="red",
     col.main = "green", col.sub = "purple")


#Examples of different settings of image

plot(x,y, type = "o", ylim = c(-2,2), col="blue")

plot(x,y, type = "p", ylim = c(-2,2), col="blue", pch=17)

plot(x,y, type = "p", ylim = c(-2,2), col="blue", pch=17, cex = 2)

plot(x,y, type = "l", ylim = c(-2,2), col="blue", lty=2)

plot(x,y, type = "l", ylim = c(-2,2), col="blue", lty=2, lwd = 3)
