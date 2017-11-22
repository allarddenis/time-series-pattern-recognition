updates = {
    'C' : {
        'out_a' : {
            'a01' : 'default_g_f'
        },
        'found' : {
            'a0' : {
                'f' : 'phi_f',
                'param1' : {
                    'f' : 'phi_f',
                    'param1' : 'D',
                    'param2' : 'delta_i_f'
                },
                'param2' : 'delta_i_f_prime'
            },
            'a1' : {
                'f' : 'phi_f',
                'param1' : 'D',
                'param2' : 'delta_i_f'
            }
        },
        'in' : {
            'a0' : {
                'f' : 'phi_f',
                'param1' : 'C',
                'param2' : {
                    'f' : 'phi_f',
                    'param1' : 'D',
                    'param2' : 'delta_i_f_prime'
                }
            },
            'a1' : {
                'f' : 'phi_f',
                'param1' : 'C',
                'param2' : {
                    'f' : 'phi_f',
                    'param1' : 'D',
                    'param2' : 'delta_i_f'
                }
            }
        }
    },
    'D' : {
        'out_r' : {
            'a01' : 'neutral_f'
        },
        'out_a' : {
            'a01' : 'neutral_f'
        },
        'maybe_b' : {
            'a01' : {
                'f' : 'phi_f',
                'param1' : 'D',
                'param2' : 'delta_i_f'
            }
        },
        'maybe_a' : {
            'a0' : {
                'f' : 'phi_f',
                'param1' : 'D',
                'param2' : 'delta_i_f_prime'
            },
            'a1' : {
                'f' : 'phi_f',
                'param1' : 'D',
                'param2' : 'delta_i_f'
            }
        },
        'found' : {
            'a01' : 'neutral_f'
        },
        'in' : {
            'a01' : 'neutral_f'
        },
        'found_e' : {
            'a01' : 'neutral_f'
        }
    },
    'R' : {
        'out_a' : {
            'a01' : {
                'f' : 'g',
                'param1' : 'R',
                'param2' : 'C'
            }
        },
        'found_e' : {
            'a0' : {
                'f' : 'g',
                'param1' : 'R',
                'param2' : {
                    'f' : 'phi_f',
                    'param1' : {
                        'f' : 'phi_f',
                        'param1' : 'D',
                        'param2' : 'delta_i_f'
                    },
                    'param2' : 'delta_i_f_prime'
                }
            },
            'a1' : {
                'f' : 'g',
                'param1' : 'R',
                'param2' : {
                    'f' : 'phi_f',
                    'param1' : 'D',
                    'param2' : 'delta_i_f'
                }
            }
        }
    }
}