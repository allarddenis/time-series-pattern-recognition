import sys, string
from datetime import datetime
import core

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

    def newLine(self, number):
        for i in list(range(0, number)):
            self.write('\n')

    def indent(self):
        self.level = self.level + 1

    def dedent(self):
        if self.level == 0:
            raise SyntaxError, "internal error in code generator"
        self.level = self.level - 1

    def writeFunction(self, patternName, featureName, aggregatorName):
        self.writeLine('def ' + aggregatorName + '_' + featureName + '_' + patternName + '(data):')
        self.indent()
        self.writeLine('C = ' + core.getInitValue('C', patternName, featureName, aggregatorName))
        self.writeLine('D = ' + core.getInitValue('D', patternName, featureName, aggregatorName))
        self.writeLine('R = ' + core.getInitValue('R', patternName, featureName, aggregatorName))
        self.writeLine('currentState = \'' + core.getInitState(patternName) + '\'')
        self.writeLine('for i in xrange(1,len(data)):')
        self.indent()
        self.writeLine('semantic = \'\'')
        self.writeLine('if(i < len(data)):')
        self.indent()
        self.writeLine('if data[i] > data[i-1]:')
        self.indent()
        self.writeLine('C_temp = C')
        self.writeLine('D_temp = D')
        self.writeLine('R_temp = R')
        for state in core.getPatternStates(patternName):
            self.writeLine('if currentState == \'' + state + '\':')
            self.indent()
            semantic = core.getNextSemantic(patternName, state, '<')
            self.writeLine('semantic = \'' + semantic + '\'')
            c_update = core.getUpdate('C', semantic, patternName, featureName, aggregatorName)
            if len(c_update) > 0:
                self.writeLine(c_update)
            self.writeLine('currentState = \'' + core.getNextState(patternName, state, '<') + '\'')
            self.dedent()
        self.dedent()
        # 

c = CodeGeneratorBackend()

c.begin(tab="    ")

c.writeLine('# --------------------------------------------------')
c.writeLine('# This file was auto-generated on ' + datetime.now().strftime('%Y-%m-%d'))
c.writeLine('# By Florine Cercle - Denis Allard')
c.writeLine('# --------------------------------------------------')
c.writeLine('')

c.writeFunction('peak', 'width', 'min')

my_file = open("generated_functions.py", "w")
my_file.write(c.end())
my_file.close()