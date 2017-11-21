import sys, string
from datetime import datetime
from input_patterns import raw_patterns
from core import Transition, State, Pattern

def getPatterns(given_patterns):
    pats = []
    for pat, pat_params in given_patterns.iteritems():
        states = []
        for name, s in pat_params['states'].iteritems():
            transitions = []
            transitions.append(Transition('<', s['<']['semantic'], s['<']['output_state']))
            transitions.append(Transition('>', s['>']['semantic'], s['>']['output_state']))
            transitions.append(Transition('=', s['=']['semantic'], s['=']['output_state']))
            new_state = State(name, s['entry'], transitions)
            states.append(new_state)
        pats.append(Pattern(pat, states))
    return pats

class CodeGeneratorBackend:

    def begin(self, tab="\t", spacer='-'):
        self.code = []
        self.tab = tab
        self.spacer = spacer
        self.level = 0

    def end(self):
        return string.join(self.code, "")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def writeComment(self, string):
        self.writeLine('# ' + string)

    def writeLine(self, string):
        self.write(string)
        self.write('\n')

    def writeTitle(self, string):
        self.writeComment(len(string) * self.spacer)
        self.writeComment(string)
        self.writeComment(len(string) * self.spacer)
        c.newLine(1)

    def writeSubTitle(self, string):
        self.writeComment(3 * self.spacer)
        self.writeComment(string)
        self.writeComment(3 * self.spacer)

    def writeFootprint(self, pattern):
        c.writeLine('def ' + pattern.name + '_footprint():')
        c.indent()

    def newLine(self, number):
        for i in list(range(0, number)):
            self.write('\n')

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

c = CodeGeneratorBackend()

c.begin(tab="    ")

c.writeLine('# --------------------------------------------------')
c.writeLine('# This file was auto-generated on ' + datetime.now().strftime('%Y-%m-%d'))
c.writeLine('# By Florine Cercle - Lisa Pasqualini - Denis Allard')
c.writeLine('# --------------------------------------------------')

patterns = getPatterns(raw_patterns)

for pat in patterns:
    c.writeTitle(pat.name)
    c.writeLine(pat.name + ' = TimeSeries(pattern)')
    c.writeSubTitle(pat.name + ' footprint')
    c.writeFootprint(pat)

c.writeTitle('NON-GENERATED MODELS')

with open('models.py', 'r') as content_file:
    content = content_file.read()
    c.writeLine(content)

my_file = open("generated_functions.py", "w")
my_file.write(c.end())
my_file.close()