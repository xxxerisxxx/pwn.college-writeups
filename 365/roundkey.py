import numpy as np
import re

#Your first state is 70366e4b3378322e73346e7b74773559
#Your second state is 7376485453796f6e6e4b306f4f7a724d
#Your second state is 71314f7d3053572e777a6433457a4d31

# Roundkey
#roundkey = ""
first = "70366e4b3378322e73346e7b74773559"
second = "7376485453796f6e6e4b306f4f7a724d"
third = "71314f7d3053572e777a6433457a4d31"
binary_a = bytes.fromhex(first).decode("utf-8")
binary_b = bytes.fromhex(second).decode("utf-8")
binary_c = bytes.fromhex(third).decode("utf-8")
#binary_round = bytes.fromhex(roundkey).decode("utf-8")

# xor both and put into matrix
#def xor_strings(xs, ys):
    #return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys)) #char to ascii to char

#xor_1 = xor_strings(binary_round, binary_a)
#xor_2 = xor_strings(binary_round, binary_b)
#xor_3 = xor_strings(binary_round, binary_c)
#print(xor_1+ xor_2+ xor_3)

# ShiftRows
n = 2
first_array = [first[i:i+n] for i in range(0, len(first), n)]
second_array = [second[i:i+n] for i in range(0, len(second), n)]
third_array = [third[i:i+n] for i in range(0, len(third), n)]

def shiftrows(A):
    arr = A
    tmp = [0] * 16
    tmp2 = [0] * 16
    
    tmp[0] = arr[0]
    tmp[1] = arr[4]
    tmp[2] = arr[8]
    tmp[3] = arr[12]

    tmp[4] = arr[13]
    tmp[5] = arr[1]
    tmp[6] = arr[5]
    tmp[7] = arr[9]

    tmp[8] = arr[10]
    tmp[9] = arr[14]
    tmp[10] = arr[2]
    tmp[11] = arr[6]

    tmp[12] = arr[7]
    tmp[13] = arr[11]
    tmp[14] = arr[15]
    tmp[15] = arr[3]

    print(arr)
    print(tmp)

    tmp2[0] = tmp[0]
    tmp2[1] = tmp[4]
    tmp2[2] = tmp[8]
    tmp2[3] = tmp[12]

    tmp2[4] = tmp[1]
    tmp2[5] = tmp[5]
    tmp2[6] = tmp[9]
    tmp2[7] = tmp[13]

    tmp2[8] = tmp[2]
    tmp2[9] = tmp[6]
    tmp2[10] =tmp[10]
    tmp2[11] = tmp[14]

    tmp2[12] = tmp[3]
    tmp2[13] = tmp[7]
    tmp2[14] = tmp[11]
    tmp2[15] = tmp[15]

    print(arr)
    print(tmp)
    print(tmp2)
    
    str_1 = ''.join(str(x) for x in tmp2) 
    line = re.sub(",", "", str_1)
    y = str_1.replace('[','').replace(']','').replace(",","").replace(' ','').replace("'","")
    toascii = bytes.fromhex(y).decode("utf-8")
    print(y)
    print(toascii)

shiftrows(first_array)
shiftrows(second_array)
shiftrows(third_array)
