#MAIN DATA TYPES: FRAMES


#DATA FRAMES

#1) Data frames differ from matrices in that columns can have different types;

#2) Data frames are very useful when you need to store statistical information in large tables;

#3) Each row corresponds to a single respondent. All information about respondents is stored in 
# columns. Each column corresponds to a different type of information (for example, one column 
#for gender, another column for education, and so on) and this information can be of different types.


#There are a lot of in-build data frames in R. You can read about them by using the command

library(help = "datasets")

#For example, let us take the dataset iris.

F<-datasets::iris

#To view the names of columns and the first few rows, you can enter the command

head(F)

#To view the structure of the data frame you can enter the command

str(F)

#Data Frame's indexation -- how to call elements of a data frame

#The same idea as for matrices. There are 2 indexes separated by a comma. 
#The first index is a condition for the row number, the second index is for the column number

#Examples:

F[2,3]                  #element that stands at the intersection of 2 row and 3 column of the frame F
F[2,]                   #elements of the 2 row of the frame F
F[,3]                   #elements of the 3  column of the frame F
F[5:10, 1:2]            #elements that stands at the intersection of 5:10 rows and 1:2 columns of the frame F

F$Sepal.Width           #elements that stands in the column named Sepal.Width 
F$Petal.Length[2:3]     ##elements that stands in the column named Petal.Length in the 2:3 rows 

#How to create a data frame

#If you need to create a data frame you can use the commands

data.frame()

#or

as.data.frame()

#Example:

N<-sample(LETTERS,1000,replace = T)
A<-sample(10:90,1000,replace = T)
G<-as.factor(sample(c('F','M'),1000,replace = T))
People<-data.frame(N,A,G)                         #creates the data frame People from vectors N,A,G
colnames(People)<-c('Name','Age','Gender')        #renames the columns of People

People[People$Gender=='F',]                       #selects data for Females
People[order(People$Age,decreasing = T),]         #order data by Age in descending order



