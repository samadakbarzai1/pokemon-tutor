import requests
from time import sleep

class Evo: 
    def evolve(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{self.name}/")
        if r.status_code == 200:
            pokemon_types = r.json()
        else:
            print(f'code not find the url please try again {r.status_code}')
            return
        r2 = requests.get(pokemon_types['evolution_chain']['url'])
        if r2.status_code == 200:
            evolving = r2.json()
            evolving = evolving['chain']
        else:
            print(f"could not find the url{r2.status_code}")
            return
        namess = evolving["species"]["name"]
        evolution = evolving['evolves_to'][0]
        evolution_name = evolution['species']['name']
        if namess == self.name:
            pass
        elif evolution_name == self.name:
            evolution_name = evolution['evolves_to'][0]['species']['name']
        else:
            print(f"You can't evolve {self.name}")
            return
        print('.......')
        sleep(1)
        print(f"Your {self.name} is evolving!?!?")
        self.display()
        sleep(1)
        print('................')
        self.name = evolution_name
        self.poke_api_call()
        self.display()

class Move():
    def __init__(self):
        self.move_list = []
        self.availableMoves = []
    def getMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
        else:
            print(f'Ran into an issue {r3.status_code}')
            return
    def teachMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
            print("following moves are availabe:")
            print(self.move_list)
            newOne = input("\nWhat you want to teach to your pokemon? ")
        else:
            print(f'again problem! {r3.status_code}')
            return
        if len(self.availableMoves) < 4:
            if newOne in self.move_list:
                print(f"TEACHING {newOne}")
                self.availableMoves.append(newOne)
            else:
                print(f"Do you see {newOne} in that move list?")
            print(f"Your {self.name} knows {self.availableMoves}")
        else:
            print("cannot choose more then 4 in a time: ")
            print(self.availableMoves)
            deleteMove = input()            
            print("You can teach the following moves:")
            print(self.move_list)
            newOne = input("\nWhat moves you want choose? ")
            if deleteMove in self.availableMoves:
                print(f"Deleting {deleteMove}")
                self.availableMoves.remove(deleteMove)
                print(f"TEACHING {newOne}")
                self.availableMoves.append(newOne)
            else:
                print(f"They do not know {deleteMove}. Please pick a move they know.")
            print(f"Your {self.name} knows {self.availableMoves}")
    
    def viewMoves(self):
        r3 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r3.status_code == 200:
            pokemon_moves = r3.json()
            self.move_list = [move['move']['name']for move in pokemon_moves['moves']]
            print(self.availableMoves)
            return
        else:
            print(f'Ran into an issue {r3.status_code}')
            return

    def program(self):        
        while True:
            response = int(input("what you want to do?\n1:- teach pokemon\n2:- view your pokemon moves\n3:- quit "))
            if response == 1:
                self.teachMoves()
            elif response == 2:
                self.viewMoves()
            elif response == 3:
                print(f"Thanks enjoy rest of the day")
                quit()
            else:
                print("Invalid input, please try again!")

class Pokemon(Move, Evo):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.types = []
        self.abilities = []
        self.weight = None
        self.image = None
        self.poke_api_call()
        
    def poke_api_call(self):
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        if r.status_code == 200:
            pokemon = r.json()
        else:
            print(f'Ran into an issue {r.status_code}')
            return
        self.name = pokemon['name']
        self.types = [pokemon['type']['name'] for pokemon in pokemon['types']]
        self.abilities = [poke['ability']['name'] for poke in pokemon['abilities']]
        self.weight = pokemon['weight'] 
        self.image = pokemon["sprites"]["front_default"]
        print(f'{self.name}!\n')
    def __repr__(self):
        return f"You caught a {self.name}!!"

obj = Pokemon("marowak-alola")
obj.program()