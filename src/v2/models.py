def signatureAsString(data):
    signature = ""
    for i in xrange(1,len(data)):
        if(i < len(data)):
            if data[i] > data[i-1]:
                signature += '<'
            elif data[i] < data[i-1]:
                signature += '>'
            else:
                signature += '='
    return signature

class TimeSeries:

    def __init__(self, data, pattern, states = None, semantic = None, footprint = None, counter = None):
        self.data = data
        self.signature = ''
        self.pattern = pattern
        self.states = states if states is not None else []
        self.semantic = semantic if semantic is not None else []
        self.footprint = footprint if footprint is not None else []
        self.counter = counter if counter is not None else []

    def getEntryState(self):
        return self.pattern.getEntryState()

    def analyze(self, data):
        self.states = []
        # Getting signature if not already done
        if self.signature == '':
            self.signature = signatureAsString(data)
        # Initiating first state
        current_state = self.getEntryState()
        self.states.append(current_state)
        self.semantic = []
        self.footprint = []
        self.counter = []
        # Initiating accumulators
        c = 0
        # Constructing semantic and states
        index = 0
        for sign in self.signature:
            next_state = self.pattern.nextState(current_state, sign)
            self.states.append(next_state['output_state'])
            current_state = next_state['output_state']
            self.semantic.append(next_state['semantic'])
            if 'found' in next_state['semantic'] :
                c += 1
            self.counter.append(c)
            index += 1
        print c
        f = False
        for sign in self.semantic[::-1]:
            if 'found' in sign or 'in' in sign:
                f = True
                self.footprint.append(c)
            elif 'maybe' in sign and f:
                self.footprint.append(c)
            elif 'out' in sign:
                if f:
                    f = False
                    c -= 1
                    self.footprint.append(0)
                else:
                    self.footprint.append(0)
            else:
                self.footprint.append(0)
        self.footprint.reverse()

class Pattern:

    def __init__(self, name, states):
        self.name = name
        self.states = states

    def nextState(self, current_state, sign):
        for state in self.states:
            if state.name == current_state:
                for transition in state.transitions:
                    if transition.sign == sign:
                        return { 'semantic' : transition.semantic_output, 'output_state' : transition.next_state }

    def getEntryState(self):
        for state in self.states:
            if state.is_entry :
                return state.name

class State:

    def __init__(self, name, is_entry, transitions):
        self.name = name
        self.is_entry = is_entry
        self.transitions = transitions

class Transition:

    def __init__(self, sign, semantic_output, next_state):
        self.sign = sign
        self.semantic_output = semantic_output
        self.next_state = next_state