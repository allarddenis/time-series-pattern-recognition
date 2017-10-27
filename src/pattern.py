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