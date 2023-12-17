import os
from sys import argv

from generator import Generator

if len(argv) < 2:
    raise Exception('Input file name is empty')

in_file_name = argv[1]
if not os.path.exists(in_file_name):
    raise Exception(f"File '{in_file_name}' was not found")

if len(argv) > 2:
    match argv[2]:
        case '--generate':
            has_generate_flag = True
        case _:
            raise Exception(f"Flag {argv[2]} is invalid")
else:
    has_generate_flag = False

with open(in_file_name) as in_file:
    gen = Generator(in_file.read())
    gen.generate()
    code_content = gen.code

if has_generate_flag:
    with open(f'translated_{in_file_name}', 'w') as out_file:
        out_file.write(code_content)
else:
    exec(code_content)
