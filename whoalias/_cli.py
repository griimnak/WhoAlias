import os

splash_text = ''' WhoAlias.py - Digital footprint lookup and handle scraper
 Author: github.com/griimnak
-------------------------------------------------------------------------------
 Please enter the main alias of desired target to begin.
 Additionally afterwards, you may enter alternative aliases for this target.
'''

def build_aliases_array():
    # All aliases
    aliases = []

    # Recycle function
    def query():
        alias = input("WhoAlias:~# ")
        return alias

    # Additional query
    def additional_query():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n [*] Enter an alternative name for this alias, or press enter to move on.")
        print(" [*] "+str(aliases)+"\n")
        real_alias = query()
        if real_alias == "":
            return aliases
        else:
            aliases.append(real_alias)
            additional_query()

    # First query
    def initial_query():
        real_alias = query()
        if real_alias == "":
            print(" [!] You need to type atleast one alias to lookup.")
            initial_query()
        else:
            aliases.append(real_alias)
            # Additional aliases
            additional_query()

    # Make the initial query
    initial_query()
    return aliases
