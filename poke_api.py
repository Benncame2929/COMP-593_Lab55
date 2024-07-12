'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests
import json


POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info('5')
    print(poke_info)
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter
    cleaned_poke_name = pokemon_name.strip().lower()

    # Build a clean URL
    POKE_API_URL = f"https://pokeapi.co/api/v2/pokemon/{cleaned_poke_name}"

    # Send a GET request
    print('Getting Pokemon info...', end="")
    resp = requests.get(POKE_API_URL)
    
    # If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp.status_code == 200:
        print("Success")
        return resp.json()
    else:
        # If the GET request failed, print the error reason and return None
        print(f" Failure :( Reason: {resp.status_code} {resp.reason}")
        return



if __name__ == '__main__':
    main()