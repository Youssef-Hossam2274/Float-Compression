import struct

def readFile(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "The file 'input.txt' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def saveFile(filename, content):
    try:
        with open(filename, "w") as file:
            file.write(content)
        return f"Content successfully saved to {filename}"
    except Exception as e:
        return f"An error occurred: {e}"

def getProbability(data: str) -> dict: 
    probabilityDic = {}
    for char in data: 
        if(char in probabilityDic):
            probabilityDic[char] += 1
        else:
            probabilityDic[char] = 1
    
    for key in probabilityDic.keys():
        probabilityDic[key] /= len(data)

    return probabilityDic

def getIndices(data: str) -> dict: 
    index = 1
    indicesDict = {}
    for char in sorted(data):
        if(char not in indicesDict): 
            indicesDict[char] = index
            index += 1
    
    return indicesDict

def getProbabilityRange(data: str, probabilityDic: dict): 
    sortedData = sorted(data)
    probabilityRange = [0]
    index = 0
    for i in range(len(sortedData)):
        if(i == 0 or (i > 0 and sortedData[i] != sortedData[i-1])):
            probabilityRange.append(probabilityDic[sortedData[i]] + probabilityRange[index])
            index += 1
    
    return probabilityRange

def floatToBinary(number):
    # Convert the float to its IEEE 754 binary representation (32-bit)
    binary_representation = ''.join(f"{c:08b}" for c in struct.pack('!f', number))
    return binary_representation

def binaryToFloat(binary_str):
    try:
        # Ensure the binary string is 32 bits
        if len(binary_str) != 32:
            raise ValueError("Binary string must be 32 bits long.")
        
        # Convert the binary string to a 32-bit integer
        int_representation = int(binary_str, 2)
        
        # Pack the integer as bytes and unpack it as a float
        float_number = struct.unpack('!f', struct.pack('!I', int_representation))[0]
        return float_number
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"