""" 
Description: 
  Creates a new PasteBin paste that contains a list of abilities 
  for a specified Pokemon

Usage:
  python pokemon_paste.py poke_name

Parameters:
  poke_name = Pokemon name
"""
import sys
import poke_api
import pastebin_api

from poke_api import get_pokemon_info
from pastebin_api import post_new_paste


def main():
    poke_name = get_pokemon_name()
    poke_info = poke_api.get_pokemon_info(poke_name)
    if poke_info is not None:
        paste_title, paste_body = get_paste_data(poke_info)
        paste_url = pastebin_api.post_new_paste(paste_title, paste_body, '1M')
        print(paste_url)

def get_pokemon_name():
    """Gets the name of the Pokemon specified as a command line parameter.
    Aborts script execution if no command line parameter was provided.

    Returns:
        str: Pokemon name
    """
    if len(sys.argv) <2:
        print("error Missing search term")
        sys.exit()

    return sys.argv[1]


def get_paste_data(pokemon_info, pokemon_name):
    """Builds the title and body text for a PasteBin paste that lists a Pokemon's abilities."""
    title = f"{pokemon_name.title()}'s Abilities"  # 
    abilities = pokemon_info.get('abilities', [])
    body_text = "Abilities:\n" + '\n'.join([ability['ability']['name'].title() for ability in abilities])
    return (title, body_text)




    if __name__ == '__main__':
        main()