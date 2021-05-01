# .....based on caesar cipher....
#......decode to be uploaded soon....
#......run the program with debugger for better results.....
def cipher():                        #encoding the message
    i = 1                 
    print("Enter the message you want to encode")
    str = input()
    print("Enter a no (this no will  be your key when you decode the message) :") #the input will be used as the key if you want to decode an encoded message
    key = int(input())
    newindex = 0
    encode = ''
    for x in range(len(str)):
        ch = str[x]
        # if i%4 == 0 :
        #     encode = encode + ch        #we will leave the 4th letter unchanged.(not NECESSARY )
        #     continue  
        if ch == " ":
            encode = encode + ch  #if blankspace, enter blankspace only
        elif ch.isdigit():
            encode = encode + ch
        elif ch.isalpha():
            ch_ascii = ord(ch.lower())      #for ascii value of c
            oldindex = ord(ch) - ord("a")
            newindex = ((oldindex + key)%26) + 97
            new_ch = chr(newindex)
            encode = encode + new_ch
        else:
            encode = encode +ch
        i=i+1
    print("The encoded string is :  " + encode)



def decipher():                   #decoding the message 
    pass                          #will be uploaded soon

print("You want to cipher(c) or decipher(d) a message...??")
print(" Enter:  c/d : ", end = " ")
a = input()

while a and a != 'e' and a != 'E':    #taking user choice
    if a == "c" or a == "C":
        cipher()                      #calling cipher function
    elif a == "d" or a=="D":
        decipher()
    else:
        print('invalid choice')
    print ('Enter your choice again(d-decipher// c-cipher// e-exit) : ')
    a = input()
print("Exiting...........")