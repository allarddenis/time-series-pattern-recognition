from inputs.input_accumulator_updates import accumulator_updates
from inputs.input_aggregators import aggregators
from inputs.input_features import features
from inputs.input_patterns import patterns

def getUpdate(accumulator, semantic, patternName, featureName, aggregatorName):
    val = ''
    if semantic in accumulator_updates[accumulator]:
        val = accumulator + ' = '
        update = accumulator_updates[accumulator][semantic]['a' + patterns[patternName]['a']]
        for element in update:
            if element == 'g':
                val = val + getValue(aggregatorName)
            elif element == 'phi_f':
                fun = features[featureName]['phi_f']
                if fun == '+':
                    val = val + 'operator.add'
                else:
                    val = val + fun
            elif element == 'delta_i_f':
                val = val + getValue(features[featureName]['delta_i_f'])
            elif element == 'delta_i_f_prime':
                if featureName == 'width':
                    val = val + '1'
                else:
                    val = val + 'data[i]'
            elif element == 'default_g_f':
                val = val + getInitValue(accumulator, patternName, featureName, aggregatorName)
            elif element == 'neutral_f':
                val = val + getValue(features[featureName]['neutral_f'])
            elif element == 'C':
                val = val + 'C_temp'
            elif element == 'D':
                val = val + 'D_temp'
            elif element == 'R':
                val = val + 'R_temp'
            else:
                val = val + element
    return val

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
        if aggregators[aggregatorName] in features[featureName]:
            val = features[featureName][aggregators[aggregatorName]]
        else:
            val = aggregators[aggregatorName]
    return getValue(val)

def getValue(val):
    if val == '+inf':
        val = 'float(\'inf\')'
    elif val == '-inf':
        val = 'float(\'-inf\')'
    elif val == 'n':
        val = 'len(data)'
    elif val == 'xi' :
        val = 'data[i-1]'
    elif val == 'delta_i_f_prime':
        val = 'data[i]'
    elif val == 'sum':
        val = 'operator.add'
    return val