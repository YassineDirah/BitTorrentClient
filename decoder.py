def decode_byte_string(bencoded_byte_string):

    if bencoded_byte_string == "0:":
            return ""
    
    if len(bencoded_byte_string)>2:
        
        colon_position = 0

        while True:
            if bencoded_byte_string[colon_position]!=":":
                colon_position+=1
            else:
                break

            if colon_position==len(bencoded_byte_string):
                break
            
        if 0<colon_position<len(bencoded_byte_string)-1:   
            try:
                string_length = int(bencoded_byte_string[:colon_position])
            except ValueError:
                raise ValueError("Invalid Byte String length")

            if len(bencoded_byte_string[colon_position+1:])==string_length:
                return bencoded_byte_string[colon_position+1:]
            
    raise ValueError("Invalid Byte String Format")
    

def isValidIntegerContent(bencoded_integer_content):
    try:
        integer_content = int(bencoded_integer_content)
    except:
        raise ValueError("Invalid Integer")

    
    if len(bencoded_integer_content)>1 and bencoded_integer_content[0]=="0" or (bencoded_integer_content[0]=="-" and bencoded_integer_content[1]=="0") :
            return False
    return True


def decode_integer(bencoded_integer):
     if len(bencoded_integer)>2 and bencoded_integer[0]=="i" and bencoded_integer[-1]=="e" and isValidIntegerContent(bencoded_integer[1:len(bencoded_integer)-1]):
          return bencoded_integer[1:len(bencoded_integer)-1]
     raise ValueError("Invalid Integer")


print(decode_integer("ite"))