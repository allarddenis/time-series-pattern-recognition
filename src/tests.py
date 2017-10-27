import signature
import occurence
import feature
import aggregation

rawData = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]

sig = signature.signatureAsString(rawData)
print sig

for match in occurence.peakRegex(sig):
    print match.group(0)