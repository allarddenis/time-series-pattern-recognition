import code_generator_backend
from datetime import datetime

c = code_generator_backend.code_generator_backend()

c.begin(tab="    ")

c.write('# -------------------------------------------------- \n')
c.write('# This file was auto-generated on ' + datetime.now().strftime('%Y-%m-%d') + '\n')
c.write('# By Florine Cercle - Lisa Pasqualini - Denis Allard')
c.write('\n# -------------------------------------------------- \n \n')

imports = [
    "pattern"
]

for imp in imports:
    c.write("import " + imp + "\n")

c.write("\n")

aggregators = [
    'max',
    'min',
    'sum'
]

def write_aggregators(key):
    for aggregator in aggregators:
        for feature in features:
            if feature != 'one':
                c.write('def ' + aggregator + '_' + feature + '_' + key + '(data): \n')
                c.indent()
                c.write('return ' + aggregator + '(' + feature + '_' + key + '(data)) \n')
                c.dedent()

features = [
    'one',
    'width',
    'height',
    'max',
    'min',
    'surface'
]

def write_features(key):
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

patterns = {
    'increasing' : "increasing = pattern.Pattern('increasing', '<', 0, 0)",
    'increasing_sequence' : "increasing_sequence = pattern.Pattern('increasing_sequence', '<(<|=)*<|<', 0, 0)",
    'increasing_terrace' : "increasing_terrace = pattern.Pattern('increasing_terrace', '<=+<', 1, 1)",
    'summit' : "summit = pattern.Pattern('summit', '(<|(<(=|<)*<))(>|(>(=|>)*>))', 1, 1)",
    'plateau' : "plateau = pattern.Pattern('plateau', '<=*>', 1, 1)",
    'proper_plateau' : "proper_plateau = pattern.Pattern('proper_plateau', '<=+>', 1, 1)",
    'strictly_increasing_sequence' : "strictly_increasing_sequence= pattern.Pattern('strictly_increasing_sequence', '<+', 0, 0)",
    'peak' : "peak = pattern.Pattern('peak', '<(=|<)*(>|=)*>', 1, 1)",
    'inflexion' : "inflexion = pattern.Pattern('inflexion', '<(<|=)*>|>(>|=)*<', 1, 1)",
    'steady' : "steady = pattern.Pattern('steady', '=', 0, 0)",
    'steady_sequence' : "steady_sequence = pattern.Pattern('steady_sequence', '=+', 0, 0)",
    'zigzag' : "zigzag = pattern.Pattern('zigzag', '(<>)+(<|<>)|(><)+(>|><)', 1, 1)"
}

for key, value in patterns.items():
    c.write('# --------------- \n')
    c.write('# ' + key + '\n')
    c.write('# --------------- \n')
    c.write("\n")
    c.write(value + "\n")
    c.write("\n")
    c.write('# --- ' + key + ' features --- \n')
    write_features(key)
    c.write("\n")
    c.write('# --- ' + key + ' aggregators --- \n')
    c.write("\n")
    write_aggregators(key)
    c.write("\n")

my_file = open("generated_functions.py", "w")
my_file.write(c.end())
my_file.close()