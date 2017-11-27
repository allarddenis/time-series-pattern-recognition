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
        failures.append(test)
    nb_tests = nb_tests + 1

print('success : ' + str(nb_success) + '/' + str(nb_tests))

if len(failures) > 0:
    print('failures' + str(failures))