from aggregators import aggregators
from data import rawData
from features import features
from patterns import patterns

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

    print C
    print D
    print R

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

    
    print signature
    print states
    print semantic

DoSomeWork(rawData, 'peak', 'width', 'min')