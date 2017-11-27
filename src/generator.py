import sys, string, time
from datetime import datetime
from generation import core 
from inputs.input_aggregators import aggregators
from inputs.input_features import features
from inputs.input_patterns import patterns

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

    def writeHeader(self, patternName, featureName, aggregatorName):
        self.writeLine('def ' + aggregatorName + '_' + featureName + '_' + patternName + '(data):')
        self.indent()

    def writeEntryState(self, patternName):
        res = 'currentState = \''
        res = res + str(core.getInitState(patternName))
        res = res + '\'\n'
        self.write(res)

    def writeInitValue(self, accumulator, patternName, featureName, aggregatorName):
        res = accumulator + ' = '
        res = res + str(core.getInitValue(accumulator, patternName, featureName, aggregatorName))
        res = res + '\n'
        self.write(res)

    def writeFunction(self, patternName, featureName, aggregatorName):
        self.writeHeader(patternName, featureName, aggregatorName)
        for accumulator in ['C', 'D', 'R']:
            self.writeInitValue(accumulator, patternName, featureName, aggregatorName)
        self.writeEntryState(patternName)
        self.writeLine('for i in xrange(1,len(data)):')
        self.indent()
        self.writeLine('if(i < len(data)):')
        self.indent()
        for accumulator in ['C', 'D', 'R']:
            self.writeLine(accumulator + '_temp = ' + accumulator)
        self.writeLine('if data[i] > data[i-1]:')
        self.writeCore(patternName, featureName, aggregatorName, '<')
        self.dedent()
        self.writeLine('elif data[i] < data[i-1]:')
        self.writeCore(patternName, featureName, aggregatorName, '>')
        self.dedent()
        self.writeLine('elif data[i] == data[i-1]:')
        self.writeCore(patternName, featureName, aggregatorName, '=')
        self.dedent()
        self.dedent()
        self.dedent()
        self.writeLine('return ' + core.getValue(aggregatorName) + '(R,C)')
        self.dedent()
        self.writeLine('')

    def writeCore(self, patternName, featureName, aggregatorName, sign):
        self.indent()
        c = True
        for state in core.getPatternStates(patternName):
            if c :
                self.writeLine('if currentState == \'' + state + '\':')
                c = False
            else:
                self.writeLine('elif currentState == \'' + state + '\':')
            self.indent()
            semantic = core.getNextSemantic(patternName, state, sign)
            for accumulator in ['C', 'D', 'R']:
                update = core.getUpdate(accumulator, semantic, patternName, featureName, aggregatorName)
                if len(update) > 0:
                    self.writeLine(update)
            self.writeLine('currentState = \'' + core.getNextState(patternName, state, sign) + '\'')
            self.dedent()

start_time = time.time()

c = CodeGeneratorBackend()

c.begin(tab="    ")

c.writeComment('----------------------------------------------------------------------------')
c.writeComment('This file was auto-generated on ' + datetime.now().strftime('%Y-%m-%d'))
c.writeComment('By Florine Cercle - Denis Allard')
c.writeComment('Source code : https://github.com/allarddenis/time-series-pattern-recognition')
c.writeComment('----------------------------------------------------------------------------')
c.writeLine('')
c.writeLine('import operator')
c.writeLine('')

nb_func = 0

for agg in aggregators:
    for feature in features:
        for pattern in patterns:
            c.writeFunction(pattern, feature, agg)
            nb_func = nb_func + 1

my_file = open("./generated/generated.py", "w")
my_file.write(c.end())
my_file.close()

exec_time = time.time() - start_time
nb_functions = len(aggregators) * len(features) * len(patterns)

print('-----')
print('status : success')
print('functions generated : %d/%d' % (nb_func, nb_functions))
print("exec time : %s seconds" % exec_time)
print('-----')