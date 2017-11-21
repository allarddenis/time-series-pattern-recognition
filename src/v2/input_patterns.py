raw_patterns = {
    'peak' : { 
        'regex' : '<(=|<)*(>|=)*>', 
        'a' : 1, 
        'b' : 1,
        'states' : {
            's': { 
                'entry' : True,
                '>' : { 'semantic' : 'out', 'output_state' : 's'},
                '=' : { 'semantic' : 'out', 'output_state' : 's'},
                '<' : { 'semantic' : 'out', 'output_state' : 'r'}
            },
            'r': { 
                'entry' : False,
                '>' : { 'semantic' : 'found', 'output_state' : 't'},
                '=' : { 'semantic' : 'maybe_b', 'output_state' : 'r'},
                '<' : { 'semantic' : 'maybe_b', 'output_state' : 'r'},
            },
            't': { 
                'entry' : False,
                '>' : { 'semantic' : 'in', 'output_state' : 't'},
                '=' : { 'semantic' : 'maybe_a', 'output_state' : 't'},
                '<' : { 'semantic' : 'out_a', 'output_state' : 'r'}
            }
        }
    },
    'increasing' : { 
        'regex' : '<', 
        'a' : 0, 
        'b' : 0,
        'states' : {
            's': { 
                'entry' : True,
                '>' : { 'semantic' : 'out', 'output_state' : 's'},
                '=' : { 'semantic' : 'out', 'output_state' : 's'},
                '<' : { 'semantic' : 'found_e', 'output_state' : 's'}
            }
        }
    },
    'increasing_terrace' : { 
        'regex' : '<=+<', 
        'a' : 1, 
        'b' : 1,
        'states' : {
            's': { 
                'entry' : True,
                '>' : { 'semantic' : 'out', 'output_state' : 's'},
                '=' : { 'semantic' : 'out', 'output_state' : 's'},
                '<' : { 'semantic' : 'out', 'output_state' : 'r'}
            },
            'r': { 
                'entry' : False,
                '>' : { 'semantic' : 'out', 'output_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'output_state' : 't'},
                '<' : { 'semantic' : 'out', 'output_state' : 'r'},
            },
            't': { 
                'entry' : False,
                '>' : { 'semantic' : 'out_r', 'output_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'output_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'output_state' : 'r'}
            }
        }
    }
}