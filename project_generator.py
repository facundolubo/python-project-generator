#!/usr/bin/env python3

#Haciendo cambios
#Aca tambien

import os


def clean_module_name(module_name):
    # Replace spaces and special characters with underscores in module name
    return ''.join(c if c.isalnum() or c.isspace() else '_' for c in module_name)

def create_tests(project_name):
    tests_dir = os.path.join(project_name, 'tests')
    # Create 'tests' directory inside the project folder if it doesn't exist
    os.makedirs(tests_dir, exist_ok=True)

def create_docs(project_name):
    docs_dir = os.path.join(project_name, 'docs')
    # Create 'docs' directory inside the project folder if it doesn't exist
    os.makedirs(docs_dir, exist_ok=True)
    with open(os.path.join(docs_dir, 'readme.md'), 'w') as docs_file:
        docs_file.write('"""\n' + 'Documentation for project' + '\n' + '"""\n')
    with open(os.path.join(docs_dir, 'requirements.txt'), 'w') as docs_file:
        docs_file.write('"""\n' + 'Requirements for project' + '\n' + '"""\n')
        docs_file.write('pytest\n')
        docs_file.write('pylint\n')
    with open('.gitignore' , 'w') as docs_file:
        docs_file.write('.venv\n')


def create_venv(project_name):
    import subprocess
    import time
    # Create a virtual environment
    subprocess.run('python3 -m venv .venv', shell=True, check=True)
    time.sleep(1)
    os.chdir(path='.venv')
    subprocess.run('source bin/activate', shell=True, check=True)
    time.sleep(1)
    # Install requirements
    subprocess.run('pip install -r docs/requirements.txt', shell=True, check=True)
    os.chdir(path='..')

def create_src(project_name):
    src_dir = os.path.join(project_name, 'src')
    # Create 'src' directory inside the project folder if it doesn't exist
    os.makedirs(src_dir, exist_ok=True)

def create_data(project_name):
    data_dir = os.path.join(project_name, 'data')
    # Create 'data' directory inside the project folder if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

def create_test_module(module_name):
    cleaned_name = clean_module_name(module_name)
    # Create 'tests' directory inside the project folder if it doesn't exist
    with open(os.path.join('./tests', f'test_{cleaned_name}.py'), 'w') as test_file:
        test_file.write('"""\n' + f'docstring for {cleaned_name}\n' + '"""\n')
        test_file.write('import unittest\n')
        test_file.write(f'import modules.{cleaned_name}\n\n')
        test_file.write(f'class Test{cleaned_name.capitalize()}Functions(unittest.TestCase):\n')
        test_file.write(f'\tdef test_{cleaned_name}(self):\n')
        test_file.write('\t\tself.assertTrue(True)  # Placeholder test case\n')

def create_project(project_name, modules):
    # Create project directory if it doesn't exist
    os.makedirs(project_name, exist_ok=True)
    os.makedirs(os.path.join(project_name, 'modules'), exist_ok=True)
    create_docs(project_name)
    create_src(project_name)
    create_data(project_name)
    create_tests(project_name)
    os.chdir('./' + project_name)
    create_venv(project_name)
    for module_name in modules:
        create_test_module(module_name)

    with open('main.py', 'w') as main_file:
        for module_name in modules:
            cleaned_name = clean_module_name(module_name)
            main_file.write(f'import tests.test_{cleaned_name} as {cleaned_name}\n')
        main_file.write('\nif __name__ == "__main__":\n')
        for module_name in modules:
            cleaned_name = clean_module_name(module_name)
            main_file.write(f'\ttest_{cleaned_name}.run_tests()\n')

    for module_name in modules:
        cleaned_name = clean_module_name(module_name)
        with open(os.path.join('modules', f'{cleaned_name}.py'), 'w') as module_file:
            module_file.write(f'def {cleaned_name}():\n')
            module_file.write(f'\tprint("Function {cleaned_name} called!")')
            module_file.write('\nif __name__ == "__main__":\n')
            module_file.write(f'\t{cleaned_name}()')
    print(f'Project {project_name} created successfully!')

if __name__ == "__main__":
    path = os.getcwd()
    project_name = input("Enter project name: ").strip()
    modules_input = input("Enter module names (comma-separated, e.g., first,second): ").strip()
    modules = [module.strip() for module in modules_input.split(',')]
    create_project(project_name, modules)
