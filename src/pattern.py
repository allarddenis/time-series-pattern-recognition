import re
import signature

class Pattern:

    def __init__(self, name, regex, a, b):
        self.name = name
        self.regex = regex
        self.a = a
        self.b = b

    def findPatterns(self, raw_data):
        sig = signature.signatureAsString(raw_data)
        matches = re.finditer(self.regex, sig)
        patterns = []
        for match in matches:
            start = match.start(0) + self.b
            end = match.end(0) - self.a
            e_occurrence = raw_data[start:end+1]
            occurrence = PatternOccurrence(match.group(0), e_occurrence, start, end)
            patterns.append(occurrence)
        return patterns

class PatternOccurrence:

    def __init__(self, s_occurrence, e_occurrence, start, end):
        self.s_occurrence = s_occurrence
        self.e_occurrence = e_occurrence
        self.start = start
        self.end = end

    def one(self):
        #TO CHANGE
        #return 1
        return self.s_occurrence

    def surface(self):
        surface = 0
        for value in self.e_occurrence:
            surface += value
        return surface

    def max(self):
        return max(self.e_occurrence)

    def min(self):
        return min(self.e_occurrence)

    def width(self):
        return self.end - self.start + 1

    def range(self):
        return max(self.e_occurrence) - min(self.e_occurrence)