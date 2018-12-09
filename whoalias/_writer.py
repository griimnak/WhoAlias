import os

class Output:
    """ Writer class
        usage: var = Output(scraper_name, alias)
               var.write("data to write")
    """
    def __init__(self, scraper_name, alias):
        """ init
            Append :param scraper_name: and :param alias:
            to :param self: and create :param self.out_path: to
            use with :def write():
        """
        self.scraper_name = scraper_name
        self.alias = alias
        self.out_path = f"output/{alias}/{scraper_name}/{scraper_name}.txt"

    def write(self, data):
        """ :param data: data string passed from outside
            Make dirs if needed and write to :param self.out_path:
        """
        try:
            # Make dirs if needed
            os.makedirs(os.path.dirname(self.out_path), exist_ok=True)

            # Open and write
            with open(self.out_path, 'a', encoding="utf-8") as out_file:
                out_file.write(f"{data}\n")
        # Ignore writing errors to avoid blocking io
        except Exception as e:
            print(" [!] [!] Ignoring error: "+str(e)+"")
            pass
