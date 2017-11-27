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

percent_success = nb_success * 100 / nb_tests

print('success : ' + str(nb_success) + '/' + str(nb_tests) + ' (' + str(percent_success) + '%)')

if len(failures) > 0:
    for fail in failures:
        print('fail : ' + str(fail))