#! /usr/bin/env python
from __future__ import print_function

import os
import sys
import logging
import cmd
from docopt import docopt

#
#  SETUP A LOGGER
#

log = logging.getLogger('onconsole')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('ONCONSOLE: [%(levelname)s] %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)

def main():
    """
    OnTalk OnConsole.
    Usage: 
      onconsole [-q] help
      onconsole [-v] [-b] [--file=SCRIPT] [-i] [COMMAND ...]
    Arguments:
      COMMAND                  A command to be executed
    Options:
      --file=SCRIPT  -f  SCRIPT  Executes the script
      -i                 After start keep the shell interactive,
                         otherwise quit [default: False]
      -b                 surpress the printing of the banner [default: False]
    """

    echo = False

    try:
        arguments = docopt(main.__doc__, help=True)
        if arguments['help']:
            arguments['COMMAND'] = ['help']
            arguments['help'] = 'False'

        script_file = arguments['--file']
        interactive = arguments['-i']
        echo = arguments['-v']
        if echo:
            pprint(arguments)
        print(arguments)

    except:
        script_file = None
        interactive = False

        arguments = {'-b': True,
                     'COMMAND': [' '.join(sys.argv[1:])]}

    cmd.Cmd.set_verbose(echo)
    cmd.Cmd.activate()
    cmd.set_verbose(echo)

    cmd.set_debug(properties["debug"])

    if arguments['-b']:
        cmd.set_banner("")
    if script_file is not None:
        cmd.do_exec(script_file)

    if len(arguments['COMMAND']) > 0:
        try:            
            user_cmd = " ".join(arguments['COMMAND'])
            if echo:
                print(">", user_cmd)
            cmd.onecmd(user_cmd)
        except Exception, e:
            Console.error("")
            Console.error("ERROR: executing command '{0}'".format(user_cmd))
            Console.error("")
            print (70 * "=")
            print(e)
            print (70 * "=")
            print(traceback.format_exc())

        if interactive:
            cmd.cmdloop()
            
    elif not script_file or interactive:
        cmd.cmdloop()

if __name__ == "__main__":
    main()
