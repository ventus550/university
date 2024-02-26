# SETTING THE COLOR IN R

# R has several possibilities for setting colors


# 1) using positive, integer numbers or the names of the colors 
#                                      0 --- "blank" 
#                                      1 --- "black" (by default)
#                                      2 --- "red"
#                                      3 --- "green3"
#                                      4 --- "blue"
#                                      5 --- "cyan"
#                                      6 --- "magenta"
#                                      7 --- "yellow"
#                                      8 --- "gray"


plot(x,y, type = "p", ylim = c(-2,2), col=6, pch=17)

plot(x,y, type = "p", ylim = c(-2,2), col=1:25, pch=17)

plot(x,y, type = "p", ylim = c(-2,2), col="skyblue", pch=17)


# 2) the command

colors()

# shows the vector of 657 color names

# The elements of this vector can be used for color settings

color=colors()
color[20:30]

#Example:

x<- seq((-4)*pi,4*pi,0.25)
y<- cos(x)

plot(x,y, type = "p", ylim = c(-2,2), col=color, pch=17)
plot(x,y, type = "p", ylim = c(-2,2), col=color[200:250], pch=17)

# 3) the color can be set as an element of palette vector using the command       

palette()

col_palette=palette()

plot(x,y, type = "p", ylim = c(-2,2), col=col_palette[6], pch=17)


# 4) the color can be set in the format RGB --  a character variable of the format  
"#RRGGBB"
#Here pairs RR, GG, BB consist of two hexadecimal digits and can therefore take values 00...FF


plot(x,y, type = "p", ylim = c(-2,2), col="#21F57A", pch=17)
plot(x,y, type = "p", ylim = c(-2,2), col="#013BFF", pch=17)


# 5) the color can be set as the function

rgb(red = ,green = ,blue = )

#where red, green, blue \in (0, 1)

rgb(0,0,1)
rgb(0,0,0.2)
rgb(0.9,0.1,0.2)

plot(x,y, type = "p", ylim = c(-2,2), col=rgb(0,0,0.2), pch=17)
plot(x,y, type = "p", ylim = c(-2,2), col=rgb(0.9,0.1,0.2), pch=17)


