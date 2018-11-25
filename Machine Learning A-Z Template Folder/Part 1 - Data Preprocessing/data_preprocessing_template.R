# Data Preprocessing 


# Importing the dataset 

dataset = read.csv("Data.csv")

# is.na (if empty....) will return true if value is missing
# ave(dataset$Age) computes average, 
# FUN = function(x) -- creating a function that is mean(x, na.rm = TRUE) -- include missing values
# third parameter is what returns if first parameter is not true
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)