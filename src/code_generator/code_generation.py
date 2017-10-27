import code_generator_backend

c = code_generator_backend.code_generator_backend()

c.begin(tab="    ")

c.write("for i in range(1000):\n")
c.indent()
c.write("print 'code generation is trivial'")
c.dedent()

print c.end()

mon_fichier = open("fichier.py", "w")
mon_fichier.write(c.end())
mon_fichier.close()