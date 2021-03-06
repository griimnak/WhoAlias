import os
import sys
import getopt


splash_text = '''
  .OOOOOOOOOOOOOOO @@                                   @@ OOOOOOOOOOOOOOOO.
  OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
  OOOOOOOOOO'''''' @@                                    @@ ```````OOOOOOOOO
  OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
  OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
  OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
  OOOOOOOOOOOOOOOOo,                                          |OOOOOOOOOOOOC
  OOOOOOOOOOOOOOOOOO                                         ,|OOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOOO @                                       |OOOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOO'@                                        OOOOOOOOOOOOOOb
  OOOOOOOOOOOOOOO'a'                                         |OOOOOOOOOOOOOy
  OOOOOOOOOOOOOO''                                        aa`OOOOOOOOOOOP
  OOOOOOOOOOOOOOb,..                                          `@aa``OOOOOOOh
  OOOOOOOOOOOOOOOOOOo                                           `@@@aa OOOOo
  OOOOOOOOOOOOOOOOOOO|                                             @@@ OOOOe
  OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
  OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
  OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
  OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
  OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
  OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
  `OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO'
'''

usage_text = "usage: whoalias.py -p <primary_alias> --alts <alt_alias> <alt_alias2> .."
help_text  = "help: whoalias.py --help"

def no_value_error(opt):
    """ Raise if option has no arg """
    print(f"You left the `{opt}` option empty.")
    sys.exit(2)

def confirm_aliases(aliases):
    print(f" [*] [*] Looking up {aliases[0]}")
    print(f" [>] [>] Full alias list for {aliases[0]}: {aliases}")
    print(" [*] [*] Confirm by typing Y or N followed by enter.\n")
    confirm = input(" Y/N:~# ")
    if confirm == "Y":
        pass
    else:
        print(" Aborted.")
        sys.exit(2)


def build_aliases_array(argv):
    """ Cli array builder
        Create short opts and long opts and help dialog
        Append values from :arg -a: and :arg --alts: to :param all_aliases:
    """

    # Create alias list
    all_aliases = []
    alt_aliases = []

    # Query cli
    try:
        opts, args = getopt.getopt(argv,"hp:a:",["primary=","alts=","help"])
        #                          args,  opts, [       long_options      ]
    except getopt.GetoptError:
        # Print hint if no options are selected
        print(usage_text)
        sys.exit(2)

    # Define options
    for opt, arg in opts:

        # Help option
        if opt in ("-h", "--help"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(splash_text)
            print('''
usage: whoalias.py -p <primary_alias> --alts <alt_alias> <alt_alias2> ..

positional arguments:
  -p, --primary    primary alias to lookup

optional arguments:
  -a, --alts       alternate aliases relevant to primary alias for lookup.
  -h, --help       show this help message and exit.
  -v, --verbosity  increase output verbosity.
            ''')

            sys.exit()

        # Primary alias option
        elif opt in ("-p", "--primary"):
            if arg == "":
                no_value_error(opt)
            # Append primary alias
            all_aliases.append(arg)

        # Alternative aliases option
        elif opt in ("-a", "--alts"):
            # :param alt_aliases: == all input after :arg -a:
            alt_aliases = sys.argv[4:]

            # Append each :param alias: in :param alt_aliases:
            for alias in alt_aliases:
                all_aliases.append(alias)

    if all_aliases == []:
        print(help_text)
        sys.exit(2)

    # Confirm and :return all_aliases:
    confirm_aliases(all_aliases)
    return all_aliases
