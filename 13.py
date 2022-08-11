import ast
my_file = open("config.json")

c = dict(ast.literal_eval(my_file.read()))
#configuration = dict(ast.literal_eval(my_file.read()))
if c["name"] == "aviel":
    print("got it")