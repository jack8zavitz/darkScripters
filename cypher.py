#function ord() would get the int value of the char.
#And in case you want to convertback after playing with the number,
#function chr() does the trick.


#There is also the unichr function, returning the Unicode character
#whose ordinal is the unichr argument:



def convertString(frase):
    splitted = list(frase)
    converted_to_ASCII = []
    for word in splitted:
        converted_to_ASCII +=[ord(word)]
    coded = []
    for number in converted_to_ASCII:
        coded +=[number*5682+6]
    return coded


###############################################################
print ("Please choose one of the following options:")
print ("\t1)Insert text here")
print ("\t2)You can put the path to the especific txt file")

option = input("Option: ")

print ("Ok. You choosed option "+option+")")

while option != "1" and option !="2":
    print("Please write 1 or 2 dumbass")
    print ("Option:")
    option=input()
###############################################################
if option =="1":
    print("Please write what you want to encript:")
    text=input()
    print (convertString(text))
    
else:
    path=input("Please write the path to you text file: ")
    with open(path, "r+") as file:
        for line in file:
            print (convertString(line))
    file.close()
    


