import signature
import pattern

raw_data = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]

peak = pattern.Pattern('peak', '<(=|<)*(>|=)*>', 1, 1)

for match in peak.findPatterns(raw_data):
    print match.start
    print match.end
    print match.s_occurrence
    print match.e_occurrence