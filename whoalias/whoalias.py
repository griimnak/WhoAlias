import os
import asyncio

from .cli import build_aliases_array, splash_text

async def test_func(text):
    print(text)

async def test_func1(word):
    await asyncio.sleep(1)
    print(word)

class WhoAlias():
    def __init__(self, all_aliases):
        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Append all aliases to WhoAlias
        print("\n [+] Appending .. "+ str(all_aliases))
        self.all_aliases = all_aliases

        # Begin event loop
        try:
            self.loop = asyncio.get_event_loop()
            self.loop.run_until_complete(self.main(all_aliases=self.all_aliases))
        except Exception as e:
            exit(str(e))
        #finally:
            #loop.close()

    async def main(self, all_aliases):
        print(" [*] Initializing WhoAlias.main() ..")

        t1 = self.loop.create_task(test_func1("Hello 1"))
        t2 = self.loop.create_task(test_func("Hello 2"))

        await asyncio.wait([t1, t2])
        return t1, t2


def run():
    # Clear console and display splash
    os.system('cls' if os.name == 'nt' else 'clear')
    print(splash_text)

    # Build aliases array
    aliases = build_aliases_array()

    # Initialize
    WhoAlias(aliases)


