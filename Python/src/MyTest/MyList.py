#!/usr/bin/env python3

def main():
    game = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print("There are",len(game),"items in list")
    print("Full list")
    print_list(game)  
    X=game.pop()
    print("--------------------------------")
    print(X)
    X=game.pop()
    print(X)
    i = game.index('Paper')
    print("--------------------------------")
    print("list after popping")
    print_list(game)
    print("--------------------------------")
    print(game[1:4])
    game.remove('Scissors')
    print(game[1:4])
    print_list(game)
    print("There are",len(game),"items in list")
    print(', '.join(game))


def print_list(o):
    for i in o:
        print(i, end=' ', flush=True)
        print()

if __name__ == '__main__':
   main()
