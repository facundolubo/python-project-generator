import os

def clean_module_name(module_name):
    # Replace spaces and special characters with underscores in module name
    return ''.join(c if c.isalnum() or c.isspace() else '_' for c in module_name)

def create_test_module(project_name, module_name):
    cleaned_name = clean_module_name(module_name)
    tests_dir = os.path.join(project_name, 'tests')
    # Create 'tests' directory inside the project folder if it doesn't exist
    os.makedirs(tests_dir, exist_ok=True)
    with open(os.path.join(tests_dir, f'test_{cleaned_name}.py'), 'w') as test_file:
        test_file.write('"""\n' + f'docstring for {cleaned_name}\n' + '"""\n')
        test_file.write('import unittest\n')
        test_file.write(f'import modules.{cleaned_name}\n\n')
        test_file.write(f'class Test{cleaned_name.capitalize()}Functions(unittest.TestCase):\n')
        test_file.write(f'\tdef test_{cleaned_name}(self):\n')
        test_file.write('\t\tself.assertTrue(True)  # Placeholder test case\n')

def create_project(project_name, modules):
    # Create project directory if it doesn't exist
    os.makedirs(project_name, exist_ok=True)
    # Create 'tests' directory inside the project folder if it doesn't exist
    os.makedirs(os.path.join(project_name, 'tests'), exist_ok=True)
    # Create 'modules' directory inside the project folder if it doesn't exist
    os.makedirs(os.path.join(project_name, 'modules'), exist_ok=True)
    os.chdir(project_name)

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
    with open('requirements.txt', 'w') as requirements_file:
        requirements_file.write('pytest\n')
        requirements_file.write('pytest-cov\n')
        requirements_file.write('pylint\n')
        requirements_file.write('flake8\n')
        requirements_file.write('black\n')

    print(f'Project {project_name} created successfully!')

if __name__ == "__main__":
    project_name = input("Enter project name: ").strip()
    modules_input = input("Enter module names (comma-separated, e.g., first,second): ").strip()
    modules = [module.strip() for module in modules_input.split(',')]

    for module_name in modules:
        create_test_module(project_name, module_name)
    create_project(project_name, modules)
