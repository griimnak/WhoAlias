import asyncio
import sys

from ._cli import build_aliases_array
from .facebook import scrape as fb_scrape
from .github import scrape as gb_scrape
from .google import scrape as go_scrape
from .instagram import scrape as ig_scrape
from .league import scrape as lg_scrape
from .twitter import scrape as tw_scrape

loop = asyncio.get_event_loop()


class WhoAlias():
    """ WhoAlias Core
        Entry point: :def run():
        :def __init__: append :param all_aliases: to :param self:
        then try to :param loop.run_until_complete(:def self.main():):
        catch exceptions and finally :def loop.close():
    """
    def __init__(self, all_aliases):
        print("\n [>] [>] Appending .. "+ str(all_aliases))

        self.all_aliases = all_aliases

        try:
            loop.run_until_complete(self.main())
        except Exception as e:
            exit(str(e))
        finally:
            loop.close()

    async def main(self):
        """ :def main():
            Dispatch all tasks then :await: and :return:
        """
        print(" [*] [*] Initializing WhoAlias.main() ..")
        # Social medias
        t1 = fb_scrape(self.all_aliases)
        t2 = tw_scrape(self.all_aliases)
        t3 = gb_scrape(self.all_aliases)
        t4 = ig_scrape(self.all_aliases)
        t5 = go_scrape(self.all_aliases)

        # Games
        # t5 = lg_scrape(self.all_aliases)

        await asyncio.wait([t1, t2, t3, t4, t5])

        print("\n\n [I= Instagram, G= Github, O= Google, F= Facebook, T= Twitter]")


def run():
    """ Runner
        Build :param aliases: then Initialize :class WhoAlias(:param aliases:):
    """
    aliases = build_aliases_array(sys.argv[1:])
    WhoAlias(aliases)


