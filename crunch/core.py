#! /usr/bin/env python
# -*- coding: utf-8 -*-

from clint import args
from clint.textui import progress, colored, puts
import multiprocessing
import os
import sys

"""
    args.all yields all the command line arguments in list.
    Also expands ~ 
    args.grouped yield --d or -d with passed params
"""
################### Constants #############################
syntax = {'usage': """
            [Usage]: crunch [primary_options] [values] 
            primary_options
            -------
            -d or --download => list of all links for downloading
            -r => read list of links from file
            --dest => destination to save files
            """,
            '-d':"""
            -d or --download => list of all links for downloading

            Example
            -------
            crunch -d https://github.com/kennethreitz/requests/tarball/master
            crunch --download https://github.com/kennethreitz/requests/tarball/master
            """,
            '-r':
            """
            -r => read list of links from file

            All links should be separated by new line.

            Example
            -------
            crunch -r links.txt
            """,
            '--dest':
            """
            --dest => destination to save files

            Example
            -------
            crunch -d https://github.com/kennethreitz/requests/tarball/master --dest downloads
            crunch --download https://github.com/kennethreitz/requests/tarball/master --dest ~/Downloads
            crunch -r links.txt --dest /home/user/Desktop

            """,
            '--help':
            """
                crunch --help [option] to know about usage of command
            """
        }

class Dependency(dict):
     """
        This is the class responsible for solving dependency.
     """
     def __init__(self):
         """
            Initialize all the values to None.
            During course of the execution set True or False
         """
         self['save_downloads'] = {'custom_dir': None, 'default_dir': True}
         self['download_urls'] = {'command_line': True, 'from_file': None}
    
def crunch_help(msg = None, menu = None):
    """
        Func responsible for printing syntax errors and help message
        :param msg => msg to print, when called by other function while parsing
                      args mismatch
        :param menu => option for which help should be displayed
    """
    if msg:
        puts(colored.red(msg))
    if menu:
        try:
            print(syntax[menu])
        except KeyError:
            message = "Displaying available options"
            puts(colored.green(message))
            puts(colored.green( '-' * len(message)))
            for key in syntax:
                puts(colored.blue(key))
            puts(colored.red(syntax['--help']))
    
def process(all_args, cwd):
    """
        Main function which will process cruncg command.

        :param all_args => all the command line arguments as OrderdDict
        :parm cwd => Current Working Directory
    """
    try:
        d = Dependency()
        urls_for_downloading = set([])
        if '-d' in all_args:
            urls_for_downloading.add(all_args['-d'].all)
        elif '--download' in all_args:
            urls_for_downloading.add(all_args['--download'].all)
        elif '--r' in all_args:
            d['download_urls']['from_file'] = True
            d['download_urls']['command_line'] = False
            from_file = all_args['--r'].all
            if len(from_file) >= 1:
                if os.path.isfile(from_file):
                    #print from_file
                    pass
                else:
                    puts(colored.red("file not found"))
            else:
                crunch_help(msg = "No File mentioned", menu = False)
        elif '-h' in all_args:
            option = all_args['-h'].all
            if option:
                for o in option:
                    crunch_help(menu = o)
            else:
                crunch_help(menu = 1) #forcing to raise key error
        elif '--h' in all_args:
            option = all_args['--h'].all
            for o in option:
                crunch_help(menu = o)
        elif '--help' in all_args:
            option = all_args['--help'].all
            print type(option)
            for o in option:
                crunch_help(menu = o)
            

        if '--dest' in all_args:
            destination = all_args['--dest']
    except KeyboardInterrupt: 
        puts(colored.red("Got keyboard Interrupt, exiting crunch"))
        sys.exit(1)

def main():
    cwd = os.getcwd()
    all_args = args.grouped
    process(all_args, cwd)



main()        
sys.exit(0)
