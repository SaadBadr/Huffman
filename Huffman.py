# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:34:20 2020

@author: Seif ElSaeed
"""
import HuffmanCodes as code
def main():
    
    
    ###ENCODING
    
    #open file and put it in a string
    with open('test.txt', 'r') as myfile:
        string = myfile.read()
    
    #Create Dictionary of Code
    dict = code.saad_please_i_need_the_codes(string)
    print(dict)
    
    #Encode string to byte array using Code Dictionary
    bitstring = ''
    for c in string:
        bitstring += dict[c]
    print(bitstring)
    bytestring = toBytes(bitstring)
    
    #write to binary file the encoded version
    with open('test.bin','wb') as file:
        file.write(bytestring)
    
    
    
    
    ###DECODING
    
    #read the data from file as bytes
    with open('test.bin','rb') as file:
        encodeddata =  file.read()
    
    #### TODO make bitstring equal
    decodedbits = toBits(encodeddata)
    
    #to check if bitstrings are equal ##they are equal except last byte
    if decodedbits == bitstring:
        print('true')
    else :
        print('false')
    
    #made decode dict
    decodedict = {}
    for key in dict:
        decodedict[dict[key]] = key
    
    #decoding bitstring
    result = ''
    result = huffmanDecode(decodedict, decodedbits)
    
    #write to decoded file
    with open('decodedtest.txt','w') as file:
        file.write(result)
    
    
    
def toBytes(bstring):
    b = bytearray()
    for i in range(0,len(bstring),8):
        b.append( int(bstring[i:i+8] , 2) )
    return bytes(b)

def toBits(bytestring):
    b = ''
    lastbyte = ''
    temp = ''
    for i in range(0,len(bytestring)-1):
        for j in range(7,-1,-1):
            b += str( (int(bytestring[i]) >> j ) & 1 )
            
    #last byte to be correct
    """
    for j in range (0,8,1):
        lastbyte = str( (int( bytestring[ len(bytestring)-1 ] ) >> j ) & 1 )
        if lastbyte == '0':
            break
        temp += lastbyte
    temp = temp[::-1] 
    b+=temp
    """    
    print(b)

def huffmanDecode (dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    print(res)
    return res
    
main()
        
    