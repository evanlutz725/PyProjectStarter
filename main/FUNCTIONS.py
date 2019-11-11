#!/usr/bin/python3
# Written by Evan Lutz 11/10/2019
# PyProjectStarter Functions

import sys
import os

def mkdir(full_directory_path):
    '''
    Makes a directory using os.system
    :param full_directory_path: string of full directory path to be made
    :return: null
    '''
    os.system('mkdir %s' %(full_directory_path))

    return None

def touch(full_file_path):
    '''
    Makes a file using os.system
    :param full_file_path: string of full file path
    :return: null
    '''
    os.system('touch %s' %(full_file_path))

    return None
