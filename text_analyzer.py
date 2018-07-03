#Character counter : By Imran CSE RU
#Enter Your file name .keep in mind that the file must be in the same folder python programm is 
filename = input("Enter file name:")
#Enter character on which you want to operate operation
check_char = input("Enter char :")
with open(filename) as f:#opening a file with variable f
    text = f.read() #read the file as variable text
print(text) #printing the file

#function to count the character how many time it appears in the file .
#count_char() function takes two argument file and char
#which are actually two variables stand for text and character variable
#a counting variable count initialize with 0 and if the desired char found in text file count increase by 1

def count_char(file,char):
    count = 0;
    for c in file:
        if c == char:
            count+=1
    return count

num_app = count_char(text,check_char)
print(num_app)#printing number of apperance the char in file
print(round(num_app*100/len(text),2))#printing the percentage of char appear in the file
