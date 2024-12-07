from utils import read_input_file, getProbability, getIndices, getProbabilityRange

def compress(inputData:str) -> float:
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
    
    return (start + end)/2
        
def main(): 
    inputData = read_input_file("input.txt")
    compressedData = compress(inputData)

    print(compressedData)


main()