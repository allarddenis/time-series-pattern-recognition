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
    }
}