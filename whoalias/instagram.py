import asyncio
import os
import re
import shutil
import json

import requests

from ._writer import Output



async def scrape(all_aliases):
    """ Instagram scrape function
        Count :param aliases_tested: and :param aliases_found:
        Run the scrape function for each :param alias: in :param all_aliases:
        :return: :param aliases_tested: and :param aliases_found:
    """
    aliases_tested = 0
    aliases_found = 0

    for alias in all_aliases:
        """ NOTE: Might add a config file to manage all URLS ..
        """
        URL = f'https://instagram.com/{alias}/'

        response = requests.get(URL)


        # Count :param aliases_tested: if :param response:
        aliases_tested += 1

        if response.status_code == 404:
            # print(f" [*] https://instagram.com/{alias}/ returned nothing ..")
            pass

        elif response.status_code == 200:
            # Count to :param aliases_found:
            aliases_found += 1

            # print(f" [>] [>] {URL} .. -> Potential match logged")

            # Get Instagram JSON from HTML because their frontend disallows traditional scraping
            json_match = re.search(r'window\._sharedData = (.*);</script>', response.text)

            profile_json = json.loads(json_match.group(1))['entry_data']['ProfilePage'][0]['graphql']['user']

            # Write profile data to txt file
            out = Output("Instagram", alias)

            # Followage and Bio
            out.write(f"Instagram summary for `{alias}` {URL}")
            out.write(f"{alias} alledged real name: {profile_json['full_name']}")
            out.write(f"{alias} has {profile_json['edge_owner_to_timeline_media']['count']} instagram posts")
            out.write(f"{alias} follows {profile_json['edge_follow']['count']} users and has {profile_json['edge_followed_by']['count']} instagram followers")
            out.write(f"'{profile_json['biography']}'")

            # Begin saving instagram photoa
            print(f" [*] [I] Cloning library of {alias} to /output/{alias}/instagram/ ..")
            count = 0
            for image_link in profile_json['edge_owner_to_timeline_media']['edges']:
                count += 1
                # Try to download, ignore if error is thrown
                try:
                    # Get image with http request
                    image = requests.get(image_link['node']['display_url'], stream=True)
                    image.raw.decode_content = True

                    # Set output format
                    image_path = f"output/{alias}/instagram/{str(count)}.jpg"

                    # print(f" [+] Downloading photo: {image_path} ..")
                    # Make dirs if needed
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)

                    # Open and write
                    with open(image_path, 'wb') as out_file:
                        shutil.copyfileobj(image.raw, out_file)
                    del image

                    await asyncio.sleep(0.01)
                except Exception as e:
                    print(" [!] Ignoring error: "+str(e)+"")
                    pass
    print(f" [*] [I] {aliases_tested} aliases tested, {aliases_found} potential Instagram matches logged.")
