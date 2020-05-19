# Llendel Reyes 818229562
# CS 496 Final Project

import sys
import random 
import pandas as pd 

def SpAttackMultiplierAgainstOpponent(Type): # function to get battle pokemon special attack effectiveness against opponent
    if Type == 'bug':
        SpecialAttackMultiplier = int(battlePokemonStats['against_bug'])
        return SpecialAttackMultiplier
    if Type == 'dark':
        SpecialAttackMultiplier = int(battlePokemonStats['against_dark'])
        return SpecialAttackMultiplier
    if Type == 'dragon':
        SpecialAttackMultiplier = int(battlePokemonStats['against_dragon'])
        return SpecialAttackMultiplier
    if Type == 'electric':
        SpecialAttackMultiplier = int(battlePokemonStats['against_electric'])
        return SpecialAttackMultiplier
    if Type == 'fairy':
        SpecialAttackMultiplier = int(battlePokemonStats['against_fairy'])
        return SpecialAttackMultiplier
    if Type == 'fighting':
        SpecialAttackMultiplier = int(battlePokemonStats['against_fight'])
        return SpecialAttackMultiplier
    if Type == 'fire':
        SpecialAttackMultiplier = int(battlePokemonStats['against_fire'])
        return SpecialAttackMultiplier
    if Type == 'flying':
        SpecialAttackMultiplier = int(battlePokemonStats['against_flying'])
        return SpecialAttackMultiplier
    if Type == 'ghost':
        SpecialAttackMultiplier = int(battlePokemonStats['against_ghost'])
        return SpecialAttackMultiplier
    if Type == 'grass':
        SpecialAttackMultiplier = int(battlePokemonStats['against_grass'])
        return SpecialAttackMultiplier
    if Type == 'ground':
        SpecialAttackMultiplier = int(battlePokemonStats['against_ground'])
        return SpecialAttackMultiplier
    if Type == 'ice':
        SpecialAttackMultiplier = int(battlePokemonStats['against_ice'])
        return SpecialAttackMultiplier
    if Type == 'normal':
        SpecialAttackMultiplier = int(battlePokemonStats['against_normal'])
        return SpecialAttackMultiplier
    if Type == 'poison':
        SpecialAttackMultiplier = int(battlePokemonStats['against_poison'])
        return SpecialAttackMultiplier
    if Type == 'psychic':
        SpecialAttackMultiplier = int(battlePokemonStats['against_psychic'])
        return SpecialAttackMultiplier
    if Type == 'rock':
        SpecialAttackMultiplier = int(battlePokemonStats['against_rock'])
        return SpecialAttackMultiplier
    if Type == 'steel':
        SpecialAttackMultiplier = int(battlePokemonStats['against_steel'])
        return SpecialAttackMultiplier
    if Type == 'water':
        SpecialAttackMultiplier = int(battlePokemonStats['against_water'])
        return SpecialAttackMultiplier
    else: # if a pokemon doesn't have a type (mainly if it doesn't have a second type)
        SpecialAttackMultiplier = 0
        return SpecialAttackMultiplier

def SpAttackMultiplierAgainstBattle(Type): # function to get opponent special attack effectiveness against battle pokemon
    if Type == 'bug':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_bug'])
        return sp_attack_multiplier_opponent
    if Type == 'dark':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_dark'])
        return sp_attack_multiplier_opponent
    if Type == 'dragon':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_dragon'])
        return sp_attack_multiplier_opponent
    if Type == 'electric':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_electric'])
        return sp_attack_multiplier_opponent
    if Type == 'fairy':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_fairy'])
        return sp_attack_multiplier_opponent
    if Type == 'fighting':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_fight'])
        return sp_attack_multiplier_opponent
    if Type == 'fire':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_fire'])
        return sp_attack_multiplier_opponent
    if Type == 'flying':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_flying'])
        return sp_attack_multiplier_opponent
    if Type == 'ghost':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_ghost'])
        return sp_attack_multiplier_opponent
    if Type == 'grass':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_grass'])
        return sp_attack_multiplier_opponent
    if Type == 'ground':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_ground'])
        return sp_attack_multiplier_opponent
    if Type == 'ice':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_ice'])
        return sp_attack_multiplier_opponent
    if Type == 'normal':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_normal'])
        return sp_attack_multiplier_opponent
    if Type == 'poison':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_poison'])
        return sp_attack_multiplier_opponent
    if Type == 'psychic':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_psychic'])
        return sp_attack_multiplier_opponent
    if Type == 'rock':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_rock'])
        return sp_attack_multiplier_opponent
    if Type == 'steel':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_steel'])
        return sp_attack_multiplier_opponent
    if Type == 'water':
        sp_attack_multiplier_opponent = int(opponentPokemonStats['against_water'])
        return sp_attack_multiplier_opponent
    else: # if a pokemon doesn't have a type (mainly if it doesn't have a second type)
        sp_attack_multiplier_opponent = 0
        return sp_attack_multiplier_opponent


def SortByType(TargetPokemonMainType): # function sort pokemon party based off the opponent's type
    if TargetPokemonMainType == 'bug':
        print("Sorting by bug...\n")
        PokemonParty["Rank"] = PokemonParty["against_bug"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'dark':
        print("Sorting by dark...\n")
        PokemonParty["Rank"] = PokemonParty["against_dark"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'dragon':
        print("Sorting by dragon...")
        PokemonParty["Rank"] = PokemonParty["against_dragon"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'electric':
        print("Sorting by electric...")
        PokemonParty["Rank"] = PokemonParty["against_electric"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'fairy':
        print("Sorting by fairy...")
        PokemonParty["Rank"] = PokemonParty["against_fairy"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'fighting':
        print("Sorting by fighting...")
        PokemonParty["Rank"] = PokemonParty["against_fight"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'fire':
        print("Sorting by fire...")
        PokemonParty["Rank"] = PokemonParty["against_fire"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty 
    if TargetPokemonMainType == 'flying':
        print("Sorting by flying...")
        PokemonParty["Rank"] = PokemonParty["against_flying"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'ghost':
        print("Sorting by ghost...")
        PokemonParty["Rank"] = PokemonParty["against_ghost"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'grass':
        print("Sorting by grass...")
        PokemonParty["Rank"] = PokemonParty["against_grass"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'ground':
        print("Sorting by ground...")
        PokemonParty["Rank"] = PokemonParty["against_ground"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'ice':
        print("Sorting by ice...")
        PokemonParty["Rank"] = PokemonParty["against_ice"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty 
    if TargetPokemonMainType == 'normal':
        print("Sorting by normal...")
        PokemonParty["Rank"] = PokemonParty["against_normal"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'poison':
        print("Sorting by poison...")
        PokemonParty["Rank"] = PokemonParty["against_poison"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'psychic':
        print("Sorting by psychic...")
        PokemonParty["Rank"] = PokemonParty["against_psychic"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'rock':
        print("Sorting by rock...")
        PokemonParty["Rank"] = PokemonParty["against_rock"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty  
    if TargetPokemonMainType == 'steel':
        print("Sorting by steel...")
        PokemonParty["Rank"] = PokemonParty["against_steel"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty
    if TargetPokemonMainType == 'water':
        print("Sorting by water...")
        PokemonParty["Rank"] = PokemonParty["against_water"].rank(method = 'first', ascending=False) 
        PokemonParty.sort_values("Rank", inplace = True) 
        PokemonParty.to_csv('SortedParty.csv')
        SortedParty = pd.read_csv("SortedParty.csv", usecols=['Rank','name', 'type1', 'type2'])
        return SortedParty

def validPokemon(userPokemon): # function to check valid pokemon names
    userPokemon = userPokemon.capitalize()
    if userPokemon not in pokemonList: 
        return False # not a valid Pokemon name 
    else:
       return True # valid Pokemon name

data = pd.read_csv("pokemon.csv")
pokemonList = data.name.tolist() # creates a list of all known pokemon, will be used to error check
invalidPokemoncount = 0
pokemonParty = [] # list for user's party pokemon

# list of all known pokemon types
pokemonTypes = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Steel', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon', 'Dark', 'Fairy']

while (1):
    print("Enter up to 6 Pokemon you want to battle with. Enter the Pokemon followed by its Type.") # prompt for user to enter their pokemon and its respective type
    print("1st Pokemon: ") # gets inputs from user
    pokemon_one = input()
    pokemon_one = pokemon_one.capitalize() # capitalizes first letter to match case sensitivity in the pokemon CSV file
    IsValid = validPokemon(pokemon_one)
    if IsValid == True:
        pokemonParty.append(pokemon_one) # added to pokemon party
        df1 = data[data['name'].str.match(pokemon_one)]
        df1.to_csv('partyPokemon.csv') 
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1 # keeps track of number of invalid pokemon entries

    print("2nd Pokemon: ") # gets inputs from user
    pokemon_two = input()
    pokemon_two = pokemon_two.capitalize()
    IsValid = validPokemon(pokemon_two)
    if IsValid == True:
        pokemonParty.append(pokemon_two)
        df2 = data[data['name'].str.match(pokemon_two)]
        df2.to_csv('partyPokemon.csv', mode='a', header=False) # appended to csv file containg only the party pokemon
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1

    print("3rd Pokemon: ") # gets inputs from user
    pokemon_three = input()
    pokemon_three = pokemon_three.capitalize()
    IsValid = validPokemon(pokemon_three)
    if IsValid == True:
        pokemonParty.append(pokemon_three)
        df3 = data[data['name'].str.match(pokemon_three)]
        df3.to_csv('partyPokemon.csv', mode='a', header=False)
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1

    print("4th Pokemon: ") # gets inputs from user
    pokemon_four = input()
    pokemon_four = pokemon_four.capitalize()
    IsValid = validPokemon(pokemon_four)
    if IsValid == True:
        pokemonParty.append(pokemon_four)
        df4 = data[data['name'].str.match(pokemon_four)]
        df4.to_csv('partyPokemon.csv', mode='a', header=False)
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1

    print("5th Pokemon: ") # gets inputs from user
    pokemon_five = input()
    pokemon_five = pokemon_five.capitalize()
    IsValid = validPokemon(pokemon_five)
    if IsValid == True:
        pokemonParty.append(pokemon_five)
        df5 = data[data['name'].str.match(pokemon_five)]
        df5.to_csv('partyPokemon.csv', mode='a', header=False)
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1

    print("6th Pokemon: ") # gets inputs from user
    pokemon_six = input()
    pokemon_six = pokemon_six.capitalize()
    IsValid = validPokemon(pokemon_six)
    if IsValid == True:
        pokemonParty.append(pokemon_six)
        df6 = data[data['name'].str.match(pokemon_six)]
        df6.to_csv('partyPokemon.csv', mode='a', header=False)
    else:
        print("Unknown Pokemon.")
        invalidPokemoncount = invalidPokemoncount + 1

    if invalidPokemoncount > 0:
        print("Invalid Pokemon Party. Please select a valid Pokemon Party.")
        invalidPokemoncount = 0 # resets counter back to 0
    else:
        print("Here is your Pokemon Party: ")
        PokemonPartyOutput = pd.read_csv("partyPokemon.csv", usecols=['name', 'type1', 'type2'])
        print(PokemonPartyOutput)
        print("Are you satisfied with your choices? Type 'Yes' to continue. Press any character to start over")
        userYesorNo = input()
        if userYesorNo == 'Yes' or userYesorNo == 'yes':
            print("Done.")
            break
        else:
            print("Deleting your Pokemon party...")
            
PokemonParty = pd.read_csv("partyPokemon.csv") # read csv containing all the info on the pokemon in the user's party 
rowNum = random.randint(0, 803) # random number generator to randomly generate an opponent pokemon
i = random.randrange(0,803)
opponentPokemon = data.loc[i]['name']
TargetPokemonMainType = data.loc[i]['type1']
TargetPokemonSecondaryType = data.loc[i]['type2']

print("Your opponent's pokemon is: ", opponentPokemon, ". It is a ", TargetPokemonMainType, ", ", TargetPokemonSecondaryType, " type.")
print("Because ", opponentPokemon, " is a", TargetPokemonMainType, ", ", TargetPokemonSecondaryType,  " type, here are your best options against it: ")

# based off target pokemon's type, rank the party pokemon by its effectiveness against target pokemon. 1 - most effective, 6 - least effective
print(SortByType(TargetPokemonMainType))

while (1): # infinite loop to prompt user to pick a pokemon to battle with

    print("Which of these Pokemon do you want to battle with?")
    battlePokemon = input()
    battlePokemon = battlePokemon.capitalize()
    if battlePokemon in pokemonParty:
        print("You are going to battle with: ", battlePokemon) # informs user of their choice
        print("Are you sure? Enter 'Yes' to continue. Enter any character to pick again.")
        userbattleYesorNo = input()
        if userbattleYesorNo == 'Yes' or userbattleYesorNo == 'yes':
            break
        else:
            print("Undoing battle Pokemon choice...")

    else:
        print("That Pokemon is not in your party. Please select a Pokemon from your party.") # notifies user that desired pokemon not in their party'''

battlePokemonStats = PokemonParty[PokemonParty['name'].str.match(battlePokemon)] 
battlePokemonStats.to_csv('battlePokemon.csv') # gets battlePokemon's stats and saves to another csv
BattlePokemonMainType = ((battlePokemonStats['type1']).to_string(index=False))
BattlePokemonSecondaryType = ((battlePokemonStats['type2']).to_string(index=False))
opponentPokemonStats = data[data['name'].str.match(opponentPokemon)]
opponentPokemonStats.to_csv('opponentPokemon.csv') # gets opponentPokemon's stats and saves to another csv

print("Pokemon Battle: ", battlePokemon, "vs.", opponentPokemon)
battle_defense_stat = int(battlePokemonStats['defense']) # gets battle pokemon's def stat and converts it to an int
opponent_defense_stat = int(opponentPokemonStats['defense']) # gets opponent pokemon's def stat and converts it to an int
battlePokemonHP = 10 * battle_defense_stat
opponentPokemonHP = 10 * opponent_defense_stat
print(battlePokemon, "HP: ", battlePokemonHP) #displays battle pokemon's starting HP
print(opponentPokemon, "HP: ", opponentPokemonHP) #displays opponent pokemon's starting HP

while(1):
    if battlePokemonHP <= 0:
        print(battlePokemon, " has fainted! ", opponentPokemon, "has won the battle!") # if battle pokemon HP reaches 0 or below zero
        break
    else:
        print("What will ", battlePokemon, " do?") # Menu to choose what battle pokemon will do 
        print("1. Attack (Base Attack)")
        print("2. Special Attack (Effectiveness based on Type)")
        print("3. Run")
        MoveChoice = input()
        MoveChoice = str(MoveChoice)
        if MoveChoice == '1':
            print(battlePokemon, " used Attack!")
            battle_attack_stat = int(battlePokemonStats['attack'])
            opponentPokemonHP = opponentPokemonHP - battle_attack_stat
            print(opponentPokemon, "HP:", opponentPokemonHP, "\n")

            if opponentPokemonHP <= 0:
                print(opponentPokemon, " has fainted! ", battlePokemon, "has won the battle!") # if opponent pokemon HP reaches 0 or below zero
                break
            else:
                opponentMove = random.randint(0, 1)

                if opponentMove == 0: # opponent uses its base attack
                    print(opponentPokemon, " used Attack!")
                    opponent_attack_stat = int(opponentPokemonStats['attack'])
                    battlePokemonHP = battlePokemonHP - opponent_attack_stat
                    print(battlePokemon, "HP:", battlePokemonHP, "\n")

                if opponentMove == 1:  # opponent uses its special attack
                    print(opponentPokemon, " used its Special Attack!")
                    opponent_sp_attack_stat = int(opponentPokemonStats['sp_attack'])
                    sp_attack_multiplier_opponent = max(SpAttackMultiplierAgainstBattle(BattlePokemonMainType), SpAttackMultiplierAgainstBattle(BattlePokemonSecondaryType))  
                    # max effectiveness between opponent pokemon two types, higher value used for special attack multiplier
                    if sp_attack_multiplier_opponent == 2:
                        print("It's super effective!.")
                    if sp_attack_multiplier_opponent == 0.5 or sp_attack_multiplier_opponent == 0.25:
                        print("It's not very effective.")
                    if sp_attack_multiplier_opponent == 0:
                        print("It has no effect on ", battlePokemon)
            
                    battlePokemonHP = battlePokemonHP - (opponent_sp_attack_stat * sp_attack_multiplier_opponent)

                    print(battlePokemon, "HP:", battlePokemonHP, "\n")

        if MoveChoice == '2':
            print(battlePokemon, " used its Special Attack!")
            battle_sp_attack_stat = int(battlePokemonStats['sp_attack'])
            sp_attack_multiplier = max(SpAttackMultiplierAgainstOpponent(TargetPokemonMainType), SpAttackMultiplierAgainstOpponent(TargetPokemonSecondaryType))  
            # max effectiveness between opponent pokemon two types, higher value used for special attack multiplier
            if sp_attack_multiplier == 2:
                print("It's super effective!.")
            if sp_attack_multiplier == 0.5 or sp_attack_multiplier == 0.25:
                print("It's not very effective.")
            if sp_attack_multiplier == 0:
                print("It has no effect on ", opponentPokemon)
            
            opponentPokemonHP = opponentPokemonHP - (battle_sp_attack_stat * sp_attack_multiplier)

            print(opponentPokemon, "HP:", opponentPokemonHP, "\n")



            if opponentPokemonHP <= 0:
                print(opponentPokemon, " has fainted! ", battlePokemon, "has won the battle!") # if opponent pokemon HP reaches 0 or below zero
                break
            else:
                opponentMove = random.randint(0, 1) # random number generator to simulate CPU picking opponent pokemon's next move

                if opponentMove == 0: # opponent uses its base attack
                    print(opponentPokemon, " used Attack!")
                    opponent_attack_stat = int(opponentPokemonStats['attack'])
                    battlePokemonHP = battlePokemonHP - opponent_attack_stat
                    print(battlePokemon, "HP:", battlePokemonHP, "\n")

                if opponentMove == 1:  # opponent uses its special attack
                    print(opponentPokemon, " used its Special Attack!")
                    opponent_sp_attack_stat = int(opponentPokemonStats['sp_attack'])
                    sp_attack_multiplier_opponent = max(SpAttackMultiplierAgainstBattle(BattlePokemonMainType), SpAttackMultiplierAgainstBattle(BattlePokemonSecondaryType))  
                    # max effectiveness between battle pokemon two types, higher value used for special attack multiplier
                    if sp_attack_multiplier_opponent == 2:
                        print("It's super effective!.")
                    if sp_attack_multiplier_opponent == 0.5 or sp_attack_multiplier_opponent == 0.25:
                        print("It's not very effective.")
                    if sp_attack_multiplier_opponent == 0:
                        print("It has no effect on ", battlePokemon)
            
                    battlePokemonHP = battlePokemonHP - (opponent_sp_attack_stat * sp_attack_multiplier_opponent)

                    print(battlePokemon, "HP:", battlePokemonHP, "\n")
                
        if MoveChoice == '3':
            print("Got away safely!")
            break
        else: # if MoveChoice is not 1, 2, or 3
            print("Invalid Move. Please enter '1', '2', or '3' to perform a move.")

    

