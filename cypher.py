#function ord() would get the int value of the char.
#And in case you want to convertback after playing with the number,
#function chr() does the trick.


#There is also the unichr function, returning the Unicode character
#whose ordinal is the unichr argument:



def encodeString(frase):
    splitted = list(frase)
    converted_to_ASCII = []
    for word in splitted:
        converted_to_ASCII +=[ord(word)]
    coded = []
    for number in converted_to_ASCII:
        coded +=[number*5682+6]
    return coded

#Strip the parentisis and try again :s
def decodeString(frase):
    type(frase)
    decoded = []
    for word in frase:
        decoded+=int(word)
    decoded = []
    for number in frase:
        decoded += int(number)/5682-6
    converted = []
    for number in decoded:
        converted += unichr(number)
    return converted
###############################################################
print ("Please choose one of the following options:")
print ("\t1)Insert message here")
print ("\t2)You can put the path to the especific txt file that you want to encode")

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
    print (encodeString(text))

    
else:
    path=input("Please write the path to you text file: ")
    with open(path, "r+") as file:
        for line in file:
            print (encodeString(line))
    file.close()
    

print ("What else do you want to do? Please choose 1, 2, 3 or 4:")
print ("\t1)Decode last encoded message")
print ("\t1)Decode a messsage someone sent me")
print ("\t3)You can write the path to the especific txt file that you want to decode")
print ("\t4)Exit the program :(")

option2 = input("Option: ")
while option2 != "1" and option2 !="2" and option2 !="3" and option2 !="4":
    print("Please write 1 or 2 dumbass")
    print ("Option:")
    option2=input()

if option2 == "1":
    print (text)
if option2 == "2":
    decodeString(input ("Copy the code and paste it here: "))
