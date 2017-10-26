from signature import signatureAsString 

def peakOccurences(signature):
    Out = True
    Maybe = False
    In = False
    buffer = ''
    occurence = ''
    occurences = []
    for s in signature:
        if s == '<':
            if Out:
                Out = False
                Maybe = True
                occurence += s
            elif Maybe:
                occurence += s
            elif In:
                Out = False
                Maybe = True
                In = False
                buffer = ''
                occurences.append(occurence)
                occurence = s
        elif s == '>':
            if Out:
                pass
            elif Maybe:
                Out = False
                Maybe = False
                In = True
                occurence += buffer
                occurence += s
            elif In:
                occurence += s
        else:
            if Out:
                pass
            elif Maybe:
                occurence += s
            elif In:
                buffer += s
    if In:
        occurences.append(occurence)
    return occurences

rawData = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]

signature = signatureAsString(rawData)

print signature

print peakOccurences(signature)