def valid(char): #func defined to check if character is within language
    if char in ['a','b','*','/','(',')']:
        return 1
    else:
        return 0

flag=0 #to act as a flag variable to indicate validity of expression

input_string = input("Enter regular expression.:")

print(input_string)
result='' #to store the valid or invalid string chain
result2='' #to act as the second line of chain with ^ pointer

for x in input_string :
    if x != ' ' and x != '\t':
        if valid(x) == 1:
            result += x
            result2 += ' '
        else:
            flag = 1
            result += x
            result2 += '^'
    elif x == '\t': #for tab case entered
        print("1")
        for y in range(4):
            result += ' '
            result2 += ' '
    else: # if character is a space
        result+=' '
        result2+=' '

if flag==0:
    print("VALID :",result)
else:
    print("INVALID :",result)
    print("         ",result2)

#the complete code plus readme posted to github
"""Github : https://github.com/ANUJDWIVDI/inputvalidator_assign """




