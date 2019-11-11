#!/usr/bin/python3
# Written by Evan Lutz 11/10/2019
# PyProjectStarter is a directory structure builder that builds the
# basic structure for a profession project by modern standards

import sys
import os
from FUNCTIONS import mkdir, touch

def main():
    
    try:
        full_file_path = sys.argv[1] 
        directory_name = sys.argv[2]
    except:
        print('\nPlease include the project name and directory name as arguments 1 and 2.\nExiting...')
        sys.exit()
    
    # Split the file path to get the project name
    file_path_split = full_file_path.split('/')
    # It's the last list item
    project_name = file_path_split[len(file_path_split) - 1]
    # Join the file path parts and ensure it ends with a '/'
    full_file_path = '/'.join(file_path_split) + '/'
    # Ensure the directory name ends with a '/'
    directory_name = directory_name.strip('/') + '/'
    # The following go in the project folder
    readme_file = full_file_path + 'README.rst'
    license_file_path = full_file_path + 'LICENSE'
    setup_file = full_file_path + 'setup.py'
    requirements_file = full_file_path + 'requirements.txt'
    # This is the code folder
    project_directory = full_file_path + directory_name
    # The following go in the code folder
    init_file = project_directory + '__init__.py'
    main_program_file = project_directory + project_name
    functions_file = project_directory + 'FUNCTIONS.py'

    directories_array = [full_file_path, project_directory]
    files_array = [readme_file, setup_file, requirements_file, init_file, \
                  main_program_file, functions_file]
    
    for directory in directories_array:
        mkdir(directory)
    
    for file_name in files_array:
        touch(file_name)
    # This one is difference because the GNU Public License is included by default,
    # as opposed to touching an empty file
    os.system('cp LICENSE.txt %s' %(license_file_path))

    # Sanity Check
    print('\nIf the next two lines are identical, then the program was successful. Otherwise, consult the errors.\n')
    print('LICENSE  %s  README.rst  requirements.txt  setup.py' %(directory_name[:-1]))
    os.system('ls %s' %(full_file_path))
    print('\nIf you made it this far, then it probably finished with no errors. Try "cd %s" and take a look around.\n' %(full_file_path))

if __name__ == '__main__':
    main()
