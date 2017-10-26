def signatureAsArray(data):
    signature = []
    for i in xrange(1,len(data)):
        if(i > 0 and i < len(data)):
            if data[i] > data[i-1]:
                signature.append('<')
            elif data[i] < data[i-1]:
                signature.append('>')
            else:
                signature.append('=')
    return signature

def signatureAsString(data):
    signature = ""
    for i in xrange(1,len(data)):
        if(i > 0 and i < len(data)):
            if data[i] > data[i-1]:
                signature += '<'
            elif data[i] < data[i-1]:
                signature += '>'
            else:
                signature += '='
    return signature

rawData = [1,1,4,8,6,2,7,1]

print signatureAsArray(rawData)
print signatureAsString(rawData)