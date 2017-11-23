patterns = {
    'peak' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'found', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
            },
            't': { 
                '>' : { 'semantic' : 'in', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 'r'}
            }
        }
    },
    'increasing' : { 
        'a' : '0', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 's'}
            }
        }
    },
    'increasing_terrace' : { 
        'a' : '1', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'},
            },
            't': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 'r'}
            }
        }
    }
}