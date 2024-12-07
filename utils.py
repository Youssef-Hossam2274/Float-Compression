def read_input_file(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "The file 'input.txt' does not exist."
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