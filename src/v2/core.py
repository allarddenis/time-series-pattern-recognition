from models import TimeSeries, Pattern, State, Transition
from patterns import raw_patterns

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

def getPattern(given_patterns, pattern_name):
    for pat, pat_params in given_patterns.iteritems():
        states = []
        if pat == pattern_name :
            for name, s in pat_params['states'].iteritems():
                transitions = []
                transitions.append(Transition('<', s['<']['semantic'], s['<']['output_state']))
                transitions.append(Transition('>', s['>']['semantic'], s['>']['output_state']))
                transitions.append(Transition('=', s['=']['semantic'], s['=']['output_state']))
                new_state = State(name, s['entry'], transitions)
                states.append(new_state)
            return Pattern(pat, states)

raw_data = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]

pattern = getPattern(raw_patterns, 'peak')

time_series = TimeSeries(pattern)

time_series.setData(raw_data)

time_series.analyze(raw_data)

print time_series.pattern.name
print time_series.semantic
print time_series.states
print time_series.footprint