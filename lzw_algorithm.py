#multi media project 
#Algorithm : LZW 
#Author : Ahmed Zakaria [Galilio]
#python3

#global varibls for GUI

compress_output = []
decompress_output = []   # For Flask GUI

def compress(string):   # compress method 
    new_dic = {}   # dic for new string
    output = []    # output
    counter = 0
    lenght = len(string)
    new_ascii_value = 256   # for new string
    tmp_two_string = ''
    case = 0   
    # Case 0 -> normal case that new string add to dic
    # Case 1 -> spical case that i found new string in dic
    for s in string:

        if case == 1:
            current_letter = tmp_two_string
            if counter == lenght-1:
                next_letter = ''
            else:
                next_letter = string[counter+1]
            new_st = current_letter+next_letter   # join current new string with the third string
            if not new_st in new_dic : # if the 3 join new string not in dic add it and switch to normal case
                new_dic[new_st] = new_ascii_value
                new_ascii_value+=1
                output.append(new_dic[current_letter])
                counter+=1
                tmp_two_string = ''
                case = 0
            else:               # if not continu in spicel case and join 4th letter
                case = 1
                tmp_two_string = new_st
                counter+=1


        else :

            current_letter = s
            if counter == lenght-1 :   # conndition to ensure that i reached end of string or not
                next_letter = ''
            else:
                next_letter = string[counter+1]
            
            new_st = current_letter+next_letter   # take current + next letter and check dic
            if not new_st in new_dic :    # if not add it to dic
                new_dic[new_st] = new_ascii_value
                new_ascii_value+=1
                output.append(ord(current_letter))
                counter+=1
                tmp_two_string = ''
                case = 0

            else: # if i found it switch to spicel case 
                case = 1
                tmp_two_string = new_st
                counter+=1


    print('output')   # printing output
    for x in output:
        print(x)
    
    print('-------------')
    print('Dic')
    for x in new_dic:   # printing dictoinary 
        print (x)

    return output


def de_compress(codes):   # decompress method takes codes from compress function

    counter = 0
    output = []
    new_dic = {}
    bef_let = ''   # before 
    new_ascii_value = 256  # starter dictionart asci value

    for x in codes:
        if counter == 0:    # this is first char it's not have before value 
            output.append(chr(x))
            bef_let = chr(x)   # put it before and take next code
            counter+=1
        else:
            if x > 255:  # if value > ascii code then it's in my dic
                for key,value in new_dic.items():
                    if value == x:  # if i found code in my dic assien it to varible
                        current_letter = key 
                        break
            else:  
                current_letter = chr(x)


            new_str = bef_let+current_letter[0]   # join before string with next string 
                                                  # index [0] to take first letter only 
            if not new_str in new_dic:  # if not new string in dic 
                new_dic[new_str]= new_ascii_value # put it in dic with new code
                new_ascii_value+=1
                bef_let = current_letter
                output.append(bef_let)
                counter+=1
    
    print('output')
    for x in output:    # printing output
        print(x)
    
    print('---------------')
    print('Dic')
    for x in new_dic:   #printing dic
        print (x)
    
    return output
            



def read_from_file(path):   # function to read data from file
    f = open(path,'r')
    return f

def _s_main():
    global compress_output
    global decompress_output   # main function 
    data = read_from_file('compress.txt')
    data = data.read()
    # compress
    print('----- Compressing data -------')
    compress_output = compress(data)

    # decompress

    print('----- decompress data ------')
    decompress_output = de_compress(compress_output)



'''
letter = 'a'
print(ord(letter))
'''

#compress('abcfghabcgheabcg')

#de_compress([97,98,99,102,103,104,256,99,260,101,262,103])

_s_main()
