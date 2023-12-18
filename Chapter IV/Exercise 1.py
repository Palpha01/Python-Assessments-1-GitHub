# Exercise 1: User information

# Develop a GUI App to create a file called 'bio.txt' and write the following information to the file asking user to enter the values (Name, Age, & Hometown)
# Each piece of data should be on a new line. Once the data has been written to the file, read the data from the file and output the data

file = open("Python-Assessments-1-GitHub/Chapter IV/Texts/Bio.txt","r")

print(file.read())