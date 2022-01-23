from datetime import date
import re

def extractTextBetweenRegexConditions(filePath,startRegexCondition=".*Sponsored.*",terminatorRegexConditions=[".*Sponsored.*",".*Like.*Comment,*"],linesBefore=1):
    with open(filePath, "r") as in_f:
        lines = in_f.readlines()
    startPositions = [line_idx for line_idx in range(len(lines)) if re.match(startRegexCondition, lines[line_idx], re.IGNORECASE) ]
    compoundRegex = "|".join(terminatorRegexConditions)
    endPositions = [line_idx for line_idx in range(len(lines)) if re.match(compoundRegex, lines[line_idx], re.IGNORECASE)]

    extractedTextList = []

    for startPosition in startPositions:

        if len(endPositions)==0 or startPosition > endPositions[-1]:
            endPosition = len(lines)
        else:
            endPosition = next(filter(lambda x: x > startPosition,endPositions))
        
        extractedTextList.append("".join(lines[max(0,startPosition-linesBefore):endPosition]))

    return extractedTextList






