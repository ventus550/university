#High-level functions (statistical):      

HIC<-HairEyeColor #Distribution of hair and eye color and sex in 592 statistics students
str(HIC)     # 3-dimensional matrix
color=colors()

#(1)

#barplot()

#One of the most popular ways to display small sets of numbers is charts 
#where each number is represented by a single column.

#https://en.wikipedia.org/wiki/Bar_chart

barplot(height, width = 1, space = NULL,
        names.arg = NULL, legend.text = NULL, beside = FALSE,
        horiz = FALSE, density = NULL, angle = 45,
        col = NULL, border = par("fg"),
        main = NULL, sub = NULL, xlab = NULL, ylab = NULL,
        xlim = NULL, ylim = NULL, xpd = TRUE, log = "",
        axes = TRUE, axisnames = TRUE,
        cex.axis = par("cex.axis"), cex.names = par("cex.axis"),
        inside = TRUE, plot = TRUE, axis.lty = 0, offset = 0,
        add = FALSE, ann = !add && par("ann"), args.legend = NULL, ...)

#main arguments:

#height - vector or matrix - 
#              If height is a vector 

data1<-HIC[,1,1] #select Male with Brown Eyes

barplot(data1) #the plot consists of a sequence of rectangular bars 
                     #with heights given by the values in the vector
col1<-c("black","brown","orange","lightyellow")

barplot(data1, col = col1) #barplot+color

barplot(data1, col = col1, main = "Hair color for Male with Brown Eyes", col.main=color[55]) #barplot+color+title

barplot(data1, col = col1, density = 20, angle = 60, border = color[55]) # #barplot+shading+border

barplot(data1, col = col1, space =  0.5) #barplot+color+space

barplot(data1, col = col1, width = 1:4) #barplot+color+width (a vector)

barplot(data1, col = col1, width = 3, xlim = c(0,25)) #barplot+color+width(a number) that requires xlim()

barplot(data1, col = col1, horiz = T, las=1)  # horizontal barplot, 
                               #"las" controls how the axis labels are located w.r.t  axes 

barplot(data1, col = col1, horiz = T, las=1, xlim = c(0,60))  # horizontal barplot+ xlim



#height - If height is a matrix:

data2<-HIC[,1,]  #select Male and Female with Brown Eyes (matrix 4x2   Hair x Gender)   
data3<-t(data2)  #select Male and Female with Brown Eyes (matrix 2x4   Gender x Hair) 


barplot(data2, col = col1)   # barplot for matrix data2
barplot(data3, col = col1[2:3])   # barplot for matrix data3

barplot(data2, col = col1, legend.text=T, args.legend=list(x="topleft"), ylim = c(0,150), main = "Hair color for people with Brown Eyes") 
                                                              # barplot for matrix data2+legend + title
barplot(data3, col = col1[2:3],legend.text=T, args.legend=list(x="topright", cex=2), main = "Hair color for people with Brown Eyes")   
                                                              # barplot for matrix data3+legend+ title


barplot(data2, col = col1, beside = T)  # barplot for matrix data2+ "besides" = T
barplot(data3, col = col1[2:3], beside = T)  # barplot for matrix data3+ "besides" = T)

barplot(data2, col = col1, beside = T,legend.text=T, args.legend=list(x="topright"), main = "Hair color for people with Brown Eyes")  # barplot for matrix data2+ "besides" = T
                    # barplot for matrix data3+ "besides" = T + legend +title
barplot(data3, col = col1[2:3], beside = T,legend.text=T, args.legend=list(x="topright", cex=2), main = "Hair color for people with Brown Eyes") 
                    # barplot for matrix data3+ "besides" = T + legend +title



#(2)

#pie()  - draw a pie chart.

#Sometimes pie charts are used for displaying data instead of barplots. 
#The idea is to show the "slices of a common pie" that get by different eaters. 

#https://en.wikipedia.org/wiki/Pie_chart


pie(x, labels = names(x), edges = 200, radius = 0.8,
    clockwise = FALSE, init.angle = if(clockwise) 90 else 0,
    density = NULL, angle = 45, col = NULL, border = NULL,
    lty = NULL, main = NULL, ...)

#main arguments:

#x - vector with nonnegative elements - this data are displayed as the areas of pie slices.

#labels - character vector - slices names

pie(data1) #pie chart

pie(data1, col = col1) #pie chart + color

pie(data1, col = col1, main = "Hair color for Male with Brown Eyes" ) #pie chart + color+ title

pie(data1, col = col1, clockwise = TRUE) #pie chart + color + clockwise

pie(data1, labels = c("superBlack","superBrown","superRed","superBlond"),col = col1) #pie chart + color+labels

pie(data1, col = col1, density = 30, angle = 30 ) #pie chart + shading

pie(data1, col = col1, radius = 1.3) #pie chart + color+ radius = 1.3

pie(data1, col = col1, radius = 1) #pie chart + color+ radius = 1

pie(data1, col = col1, radius = 0.5) #pie chart + color+ radius = 0.5

pie(data1, col = col1, border = 6, lwd = 3) #pie chart + color+border

pie(data1, col = col1, edges = 12) #pie chart + color+edges


par(mfrow=c(1,2))
pie(HIC[,1,1], col = col1, main = "Hair color for Male with Brown Eyes" ) 
pie(HIC[,1,2], col = col1, main = "Hair color for Female with Brown Eyes" ) 
par(mfrow=c(1,1))



#(3)

#mosaicplot()

#graphical method for visualizing data from two or more qualitative variables

#https://en.wikipedia.org/wiki/Mosaic_plot

mosaicplot(x, ...)

# x - data (table, frame, matrix...)

mosaicplot(HIC[,1,1], color = col1[2:3]) #mosaicplot for 1-dimensional matrix

mosaicplot(HIC[,,1], color = col1[2:3]) #mosaicplot for 2-dimensional matrix

mosaicplot(HIC, color = col1[2:3]) #mosaicplot for 3-dimensional matrix



#(4)

#pairs()    produce scatterplots for matrix columns 

#Let's say there is a data frame that contains the values of various numeric variables (characteristics) for objects. 
#How to start a study is to look at the data. If there are many objects, viewing the numeric table doesn't help much.
#There is a much better idea to investigate the data is presenting the data on a plot.
#I t assumed that each object corresponds to a point on the plane with coordinates defined by certain variables 
#of this object. 

#https://en.wikipedia.org/wiki/Scatter_plot


pairs(x, ...)

# x - numeric data (data frame, matrix)

str(iris)

pairs(iris[,3:4])    #scatterplot for 2 variables
pairs(iris[,3:4], pch=19)   #scatterplot+pch
pairs(iris[,3:4], pch=19, col=color[as.numeric(iris[,5])+30]) #scatterplot+pch+color (corresponding to Spicies)


#the same
plot(iris$Petal.Width~iris$Petal.Length, pch=19)
abline(lm(iris$Petal.Width~iris$Petal.Length),col="red") # the line, the sum of the distances from which to all points is minimal (linear regression) 

pairs(iris[,1:4])    #scatterplots for 4 variables
pairs(iris[,1:4], lower.panel=NULL) #scatterplots for 4 variables, without lower panel

pairs(iris[,1:4],col=color[as.numeric(iris[,5])+30],lower.panel=NULL,pch=as.numeric(iris[,5]))
#scatterplots for 4 variables, without lower panel + color (corresponding to Spicies) + pch (corresponding to Spicies)

pairs(iris[,1:4],col=color[as.numeric(iris[,5])+30],lower.panel=NULL,pch=as.numeric(iris[,5]))
par(xpd=TRUE)  #this option allows to draw a legend outside of the main plt
legend("bottomleft",title="Species:",legend=c('setosa','versicolor','virginica'),pch=c(1,2,3), col=color[31:33])


#(5)

#hist() - computes a histogram of the given data values

#https://en.wikipedia.org/wiki/Histogram

#A histogram is the most popular way to graphically display the distribution of numeric data. 
#There are absolute and relative frequency histograms

#1) histogram of absolute frequencies (the height of each column is equal to the number of sample elements 
#that belongs to the given segment)

# 2) histogram of relative frequencies (the height of each column is equal to the number of sample elements 
#that belongs to given segment divided by the size of sample)

#Let (x_1,...,x_n) be a random sample that takes values in the segment [a,b]. Let us divide [a,b] on k intervals 
#of the same width h=(b-a)/k
#Let n_i be the number of observed values within i-th interval, h_i be the hight of i-th column

#Then
#1) h_i=n_i
#2) h_i=n_i/n

#Note that the histograms of relative frequencies is useful for estimation of pdf (probability density function)

hist(x, breaks = "Sturges",
     freq = NULL, probability = !freq,
     include.lowest = TRUE, right = TRUE,
     density = NULL, angle = 45, col = NULL, border = NULL,
     main = paste("Histogram of" , xname),
     xlim = range(breaks), ylim = NULL,
     xlab = xname, ylab,
     axes = TRUE, plot = TRUE, labels = FALSE,
     nclass = NULL, warn.unused = TRUE, ...)

#main arguments:

#x - the data set that the histogram is based on;

# breaks -  the parameter that controls the selection of split points
#           By default breaks is selected by Sturgess' formula: k=[1+log_2 (n)]
#           If
#           Breaks= number : a number of split points
#           Breaks= vector : coordinates of split points

#freq = NULL                 - logical - TRUE for histogram of absolute frequencies, FALSE for histogram of relative frequencies
#or
#probability = !freq         - logical - TRUE for histogram of relative frequencies, FALSE for histogram of absolute frequencies


str(iris)
sw<-iris$Sepal.Width

hist(sw)    #histogram for Sepal.Width

par(mfrow=c(1,2))
hist(sw)                   #histogram of absolute frequencies for Sepal.Width
hist(sw, freq = FALSE)     #histogram of relative frequencies for Sepal.Width
par(mfrow=c(1,1))

par(mfrow=c(1,2))          #histograms of absolute and relative frequencies, comparison with pdf
hist(iris$Sepal.Width) 
curve(dnorm(x,mean=mean(sw),sd=sd(sw)),2,4.5,col="red",lwd=2,add=T) 
hist(iris$Sepal.Width, freq = FALSE) 
curve(dnorm(x,mean=mean(sw),sd=sd(sw)),2,4.5,col="red",lwd=2,add=T) 
par(mfrow=c(1,1))

par(mfrow=c(2,2))          #histogram for different values of the parameter "break"
hist(sw, breaks = 2)
hist(sw, breaks = 4)
hist(sw, breaks = 12)
hist(sw, breaks = 18)

hist(sw, breaks = c(2,3.5,4.5,5))
hist(sw, breaks = seq(2,5,0.5))
hist(sw, breaks = seq(2,5,0.25))
hist(sw, breaks = c(seq(2,3.5,0.25),5))
par(mfrow=c(1,1))


hist(sw, col = color[25:35])      #histogram +color
hist(sw, col = color[25:35],density = 20,angle = 20)      #histogram +shading
hist(sw, col = color[25:26], main = "Sepal Width")      #histogram +color+title
hist(sw, col = color[25:26], main = "Sepal Width",xlab = NULL)      #histogram +color+title+xlab=NULL


par(mfrow=c(2,2))          #histogram for different values of the parameter "break"
hist(iris$Sepal.Length, col = color[25:26], main = "Sepal Length",xlab = NULL)
hist(iris$Sepal.Width, col = color[25:26], main = "Sepal Width",xlab = NULL)
hist(iris$Petal.Length, col = color[25:26], main = "Petal Length",xlab = NULL)
hist(iris$Petal.Width, col = color[25:26], main = "Petal Width",xlab = NULL)
par(mfrow=c(1,1))
