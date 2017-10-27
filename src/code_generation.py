import code_generator_backend
from datetime import datetime

aggregators = [
    'max',
    'min',
    'sum'
]

features = [
    'one',
    'width',
    'height',
    'max',
    'min',
    'surface'
]

patterns = {
    'increasing' : { 
        'regex' : '<', 
        'a' : 0, 
        'b' : 0
    },
    'increasing_sequence' : {
        'regex' : '<(<|=)*<|<',
        'a' : 0,
        'b' : 0
    },
    'increasing_terrace' : {
        'regex' : '<=+<',
        'a' : 1,
        'b' : 1
    },
    'summit' : {
        'regex' : '(<|(<(=|<)*<))(>|(>(=|>)*>))',
        'a' : 1,
        'b' : 1
    },
    'plateau' : {
        'regex' : '<=*>',
        'a' : 1,
        'b' : 1
    },
    'proper_plateau' : {
        'regex' : '<=+>',
        'a' : 1,
        'b' : 1
    },
    'strictly_increasing_sequence' : {
        'regex' : '<+',
        'a' : 0,
        'b' : 0
    },
    'peak' : {
        'regex' : '<(=|<)*(>|=)*>',
        'a' : 1,
        'b' : 1
    },
    'inflexion' : {
        'regex' : '<(<|=)*>|>(>|=)*<',
        'a' : 1,
        'b': 1
    },
    'steady' : {
        'regex' : '=',
        'a' : 0,
        'b' : 0
    },
    'steady_sequence' : {
        'regex' : '=+',
        'a' : 0,
        'b' : 0
    },
    'zigzag' : {
        'regex' : '(<>)+(<|<>)|(><)+(>|><)',
        'a' : 1,
        'b' : 1
    }
}

# -----------------
# Helping functions

def write_pattern_name(key):
    c.write('\n# --------------------------------------------------------------------------- \n')
    c.write('# ' + key.upper() + '\n')
    c.write('# --------------------------------------------------------------------------- \n')
    c.write("\n")

def write_features(key):
    c.write('\n# --- ' + key + ' features --- \n \n')
    for feature in features:
        c.write('def ' + feature + '_' + key + '(data): \n')
        c.indent()
        c.write('matches = ' + key + '.findPatterns(data) \n')
        c.write('result = []\n')
        c.write('for match in matches:\n')
        c.indent()
        c.write('result.append(match.' + feature + '()) \n')
        c.dedent()
        c.write('return result \n')
        c.dedent()

def write_aggregators(key):
    c.write('\n# --- ' + key + ' aggregators --- \n \n')
    for aggregator in aggregators:
        for feature in features:
            if feature != 'one':
                c.write('def ' + aggregator + '_' + feature + '_' + key + '(data): \n')
                c.indent()
                c.write('return ' + aggregator + '(' + feature + '_' + key + '(data)) \n')
                c.dedent()

# ---------------
# Code generation

c = code_generator_backend.code_generator_backend()

c.begin(tab="    ")

c.write('# -------------------------------------------------- \n')
c.write('# This file was auto-generated on ' + datetime.now().strftime('%Y-%m-%d') + '\n')
c.write('# By Florine Cercle - Lisa Pasqualini - Denis Allard')
c.write('\n# -------------------------------------------------- \n \n')

c.write('from pattern import Pattern')

c.write("\n")

for key, value in patterns.items():
    # write pattern name
    write_pattern_name(key)
    # create pattern instance
    c.write(key + " = Pattern('" + key + "', '" + value['regex'] + "', " + str(value['a']) + ", " + str(value['b']) + ")\n")
    # write features functions
    write_features(key)
    # write aggregators
    write_aggregators(key)

my_file = open("generated_functions.py", "w")
my_file.write(c.end())
my_file.close()