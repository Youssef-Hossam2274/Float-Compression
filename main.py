from utils import readFile, getProbability, getIndices, getProbabilityRange, floatToBinary, binaryToFloat, saveFile

def compress(inputData:str):
    probabilityDic = getProbability(inputData)
    indicesDict = getIndices(inputData)
    probabilityRange = getProbabilityRange(inputData, probabilityDic)
    start = 0
    end = 1



    for char in inputData:
        charIdx = indicesDict[char]
        range = end-start
        newStart = start + (range* probabilityRange[charIdx-1])
        newEnd = start + (range*probabilityRange[charIdx])

        start = newStart
        end = newEnd

    compressedValue = (start+end)/2
    compressedBinary = floatToBinary(compressedValue)

    savedResult = f"length:{len(inputData)}\nCompressed Value:{compressedValue}\nCompressed Binary:{compressedBinary}\n"
    for key in probabilityDic.keys():
        savedResult += f"{key}:{probabilityDic[key]}\n"
    
    saveFile("output.txt", savedResult)
    

def decompress() -> str:
    
    # read file and prepare 

    fileContent = readFile("output.txt").split("\n")
    length = int(fileContent[0].split(":")[1])
    compressedValue = binaryToFloat(fileContent[2].split(":")[1])
    probabilityDic = {}
    for row in fileContent[3:]:
        # save gaurd to avoid the empty line
        if(row == ""):continue

        rowSplited = row.split(":")
        key = rowSplited[0]
        value = rowSplited[1]
        probabilityDic[key] = float(value)

    
    
    # Compute the probability ranges
    sortedChars = sorted(probabilityDic.keys())
    probabilityRange = [0]
    for char in sortedChars:
        probabilityRange.append(probabilityDic[char] + probabilityRange[-1])
    
    
    decodedString = ""
    for _ in range(length):
        for i in range(1, len(probabilityRange)):
            if probabilityRange[i-1] <= compressedValue < probabilityRange[i]:
                decodedChar = sortedChars[i-1]
                decodedString += decodedChar
                # Narrow the range for the next iteration
                rangeWidth = probabilityRange[i] - probabilityRange[i-1]
                compressedValue = (compressedValue - probabilityRange[i-1]) / rangeWidth
                break
    
    
    print(f"Decompress: {decodedString}")
    return decodedString


def main(): 
    inputData = readFile("input.txt")
    compress(inputData)
    decompress()


main()