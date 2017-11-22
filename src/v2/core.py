from aggregators import aggregators
from data import rawData
from features import features
from patterns import patterns
from accumulator_updates import updates

def getUpdate(accumulator, semantic, patternName, featureName, aggregatorName):
    val = accumulator + ' = '
    if semantic in updates[accumulator]:
        if 'a01' in updates[accumulator][semantic]:
            if updates[accumulator][semantic]['a01'] == 'default_g_f':
                val = val + getGeneratedValue(features[featureName][aggregators[aggregatorName]])
            elif 'f' in updates[accumulator][semantic]['a01']:
                if updates[accumulator][semantic]['a01']['f'] == 'phi_f':
                    val = val + features[featureName]['phi_f']
        return val
    else:
        return ''

def getNextSemantic(patternName, currentState, sign):
    return patterns[patternName]['states'][currentState][sign]['semantic']

def getNextState(patternName, currentState, sign):
    return patterns[patternName]['states'][currentState][sign]['next_state']

def getPatternStates(patternName):
    return patterns[patternName]['states']

def getInitState(patternName):
    return patterns[patternName]['entry']

def getInitValue(accumulator, patternName, featureName, aggregatorName):
    val = ''
    if accumulator == 'D':
        val = features[featureName]['neutral_f']
    else :
        val = features[featureName][aggregators[aggregatorName]]
    return getGeneratedValue(val)

def getGeneratedValue(val):
    if val == 'inf':
        val = 'float(\'inf\')'
    elif val == '-inf':
        val = 'float(\'-inf\')'
    elif val == 'n':
        val = 'len(data)'
    return val


def GetTransition(pattern, currentState, sign):
    return pattern['states'][currentState][sign]

def GetSemantic(pattern, currentState, sign):
    return pattern['states'][currentState][sign]['semantic']

def GetNextState(pattern, currentState, sign):
    return pattern['states'][currentState][sign]['next_state']

def DoSomeWork(data, pattern, feature, aggregator):

    pat = patterns[pattern]

    signature = []
    states = []
    semantic = []

    currentState = pat['entry']
    states.append(currentState)

    C = features[feature][aggregators[aggregator]]
    D = features[feature]['neutral_f']
    R = C

    for i in xrange(1,len(data)):
        if(i < len(data)):
            sign = ''
            if data[i] > data[i-1]: # '<'
                sign = '<'
            elif data[i] < data[i-1]: # '>'
                sign = '>'
            else: # '='
                sign = '='
            transition = GetTransition(pat, currentState, sign)
            signature.append(sign)
            currentState = transition['next_state']
            states.append(currentState)
            semantic.append(transition['semantic'])