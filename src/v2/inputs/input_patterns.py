patterns = {
    'bump_on_decreasing_sequence' : { 
        'a' : '1', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'out', 'next_state' : 't'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            't': { 
                '>' : { 'semantic' : 'out', 'next_state' : 't'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'u'}
            },
            'u': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'v'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 's'}
            },
            'v': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 't'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 's'}
            }
        }
    },
    'decreasing' : { 
        'a' : '0', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            }
        }
    },
    'decreasing_sequence' : { 
        'a' : '0', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'found', 'next_state' : 't'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            't': { 
                '>' : { 'semantic' : 'in', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 's'}
            }
        }
    },
    'decreasing_terrace' : { 
        'a' : '1', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            't': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 's'}
            }
        }
    },
    'dip_on_increasing_sequence' : { 
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
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 't'}
            },
            't': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'u'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 't'}
            },
            'u': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'v'}
            },
            'v': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 't'}
            }
        }
    },
    'gorge' : { 
        'a' : '1', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'u'},
                '<' : { 'semantic' : 'found', 'next_state' : 't'}
            },
            't': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'in', 'next_state' : 't'}
            },
            'u': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'u'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 's'}
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
    'increasing_sequence' : { 
        'a' : '0', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'found', 'next_state' : 't'}
            },
            't': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'in', 'next_state' : 't'}
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
                '<' : { 'semantic' : 'out', 'next_state' : 'r'}
            },
            't': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 'r'}
            }
        }
    },
    'inflexion' : { 
        'a' : '1', 
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 't'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'r'}
            },
            't': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 'r'}
            }
        }
    },
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
    'plain' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 's'},
            },
            't': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 's'}
            }
        }
    },
    'plateau' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out', 'next_state' : 'r'},
            },
            't': { 
                '>' : { 'semantic' : 'found_e', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 'r'}
            }
        }
    },
    'proper_plain' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'},
            },
            't': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'found_e', 'next_state' : 's'}
            }
        }
    },
    'proper_plateau' : {
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
                '>' : { 'semantic' : 'found_e', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 'r'}
            }
        }
    },
    'steady' : {
        'a' : '0',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'found_e', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            }
        }
    },
    'steady_sequence' : {
        'a' : '0',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'found', 'next_state' : 'r'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '=' : { 'semantic' : 'in', 'next_state' : 'r'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 's'}
            }
        }
    },
    'strictly_decreasing_sequence' : {
        'a' : '0',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'found', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'in', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 's'}
            }
        }
    },
    'strictly_increasing_sequence' : {
        'a' : '0',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'found', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '=' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '<' : { 'semantic' : 'in', 'next_state' : 'r'}
            }
        }
    },
    'summit' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 's'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'found', 'next_state' : 'r'}
            },
            'r': { 
                '>' : { 'semantic' : 'found', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'u'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'r'}
            },
            't': { 
                '>' : { 'semantic' : 'in', 'next_state' : 't'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 'r'}
            },
            'u': { 
                '>' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'u'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'r'}
            }
        }
    },
    'valley' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'r'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 's'}
            },
            'r': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_b', 'next_state' : 'r'},
                '<' : { 'semantic' : 'found', 'next_state' : 't'}
            },
            't': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 'r'},
                '=' : { 'semantic' : 'maybe_a', 'next_state' : 't'},
                '<' : { 'semantic' : 'in', 'next_state' : 't'}
            }
        }
    },
    'zigzag' : {
        'a' : '1',
        'entry' : 's',
        'states' : {
            's': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'd'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'a'}
            },
            'a': { 
                '>' : { 'semantic' : 'maybe_b', 'next_state' : 'b'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'out', 'next_state' : 'a'}
            },
            'b': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'd'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'found', 'next_state' : 'c'}
            },
            'c': { 
                '>' : { 'semantic' : 'in', 'next_state' : 'f'},
                '=' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '<' : { 'semantic' : 'out_a', 'next_state' : 'a'}
            },
            'd': { 
                '>' : { 'semantic' : 'out', 'next_state' : 'd'},
                '=' : { 'semantic' : 'out', 'next_state' : 's'},
                '<' : { 'semantic' : 'maybe_b', 'next_state' : 'e'}
            },
            'e': { 
                '>' : { 'semantic' : 'found', 'next_state' : 'f'},
                '=' : { 'semantic' : 'out_r', 'next_state' : 's'},
                '<' : { 'semantic' : 'out_r', 'next_state' : 'a'}
            },
            'f': { 
                '>' : { 'semantic' : 'out_a', 'next_state' : 'd'},
                '=' : { 'semantic' : 'out_a', 'next_state' : 's'},
                '<' : { 'semantic' : 'in', 'next_state' : 'c'}
            }
        }
    }
}