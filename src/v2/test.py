from inputs.input_tests import tests
from generated import generated

nb_success = 0
nb_tests = 0
failures = []

for test in tests:
    function = getattr(generated, test)
    data = tests[test]['data']
    res = function(data)
    if(res == tests[test]['result']):
        nb_success = nb_success + 1
    else:
        failures.append(test + ' : ' + str(res) + ' instead of ' + str(tests[test]['result']))
    nb_tests = nb_tests + 1

print('success : ' + str(nb_success) + '/' + str(nb_tests))

if len(failures) > 0:
    for fail in failures:
        print('fail : ' + str(fail))

def min_width_decreasing_sequence(sequence):
    n = len(sequence)
    c=n
    d=0
    r=n
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_tmp = d+delta+deltaprime
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+deltaprime
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+deltaprime
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = n
                    d_tmp = 0
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
        previous_number = number
    return min(r,c)

# print min_width_decreasing_sequence([3,4,2,2,5,6,6,4,4,3,1,1,4,6,4,4])