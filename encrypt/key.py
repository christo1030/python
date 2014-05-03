def  k( ):
    key = list("2434131")
    return key
    
def encript():
   
    message = raw_input(" enter your message: ")
    messageL =list(message)
#     messLength = len(messagel)
#     messagel.reverse()
#     messageFirstQ = list (reversed(messagel[:messLength/4]))
#     messageSecondQ = list(reversed(messagel[messLength/4:messLength/2]))
#     messageThirdQ = list(reversed(messagel[messLength/2:(messLength/2 + messLength/4)]))
#     messageLastQ = list(reversed(messagel[(messLength/2 + messLength/4):])) 
#     messageL = messageFirstQ + messageSecondQ + messageThirdQ + messageLastQ
    inserted = list(k()) #k() is just a function that returns the key
    
    encriptMess = list()
    # increments though message and key
    for messE in messageL:
        for keyE in inserted:
            messE = chr((ord (messE) + int(keyE) ))   # uses key and message value adding to change each char
            #print messE
            encriptMess.append(messE) # adds to new list
            
    print ''.join([str(item) for item in encriptMess])  # print
            
            


def decode():
    i =0
    j= 0
    message = raw_input(" enter Encripted message ")
    messageL =list(message)
    inserted = list(k())
    keyL = len(inserted)
    decriptMess = list()
   # decriptMess.append(chr(ord(messageL[i]) - int(inserted[i])))
    
    for elm in messageL:          #increment through list
        if not i %(keyL) :        # uses to match lenght of key
         #   if not i ==1:
          decriptMess.append(chr(ord(messageL[i]) - int(inserted[j])))      # uses key and encript char to decript to get orig char
        i = i+1
#     messagel.reverse()
#     messageFirstQ = list (reversed(messagel[:messLength/4]))
#     messageSecondQ = list(reversed(messagel[messLength/4:messLength/2]))
#     messageThirdQ = list(reversed(messagel[messLength/2:(messLength/2 + messLength/4)]))
#     messageLastQ = list(reversed(messagel[(messLength/2 + messLength/4):])) 
#     messageL = messageFirstQ + messageSecondQ + messageThirdQ + messageLastQ
            
        
    
            
    print ''.join([str(item) for item in decriptMess])   # print
    
if __name__ == '__main__':    
    decode()