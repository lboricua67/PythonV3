#!/usr/bin/env python3

def main():
    animals = dict(kitten = 'meow', puppy = 'ruff', lion = 'grr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')

    animal2 = dict(cow = 'moo', bird = 'tweek')
    animals.update(animal2)
    # Print all methods within animals dictionary
    print(dir(animals))
    # Prints size of item in memory
    print(animals.__sizeof__())
    print('-----------------------------------------')
    # Print length of dictionary
    print(len(animals))
    # Print key and values using items method
    for k, v in animals.items():
        print(f'{k}: {v}')
    print('-----------------------------------------')
    # Print keys in the dictionary
    for k in animals.keys():
        print(k)
    print('-----------------------------------------')
    # Print values in dictionary only
    for k in animals.values():
        print(k)
    print('-----------------------------------------')
    # Printing just via item
    print(animals['lion'])
    print('-----------------------------------------')
    # Print searching dictionary
    print('lion was found!' if 'lion' in animals else 'nope!')
    print('godzilla found!' if 'godzilla' in animals else 'nope! godzilla not here')
    print('-----------------------------------------')
    # checking if key exists will return value, if not, it will return value "None"
    print(animals.get('godzilla'))
    print(animals.get('dragon'))
    print('-----------------------------------------')
    # Using Pop and removes it from the dictionary
    print(animals.pop('puppy'))
    print(animals.popitem())
    print('-----------------------------------------')
    # Deleting item from dictionary
    del animals["kitten"]
    print('-----------------------------------------')
    #animals.clear()
    # Prints size of item in memory
    print(animals.__sizeof__())
    print('-----------------------------------------')
    # Print dictionary using object
    print_dict(animals)
    print(len(animals))
    animals.clear()
    print(animals.__sizeof__())
    animals.update(animal2)
    print(animals)

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')


if __name__ == '__main__':
   main()
