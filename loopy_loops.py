if __name__ == "__main__":
    
 #pokemon stuff lives here   
    pokemon = ('pikachu', 'charmander', 'bulbasaur')
    print(pokemon[1])

    pokemon.sort()
    print(pokemon)

#name tuple here
    my_name = ('Lita Martinez')
    tuple(my_name)

    if 'i' in tuple:
            print('I see you have an I!')
    else:
            print('Nope. Would you like to buy a vowel?')
    
 #for loop
    for i in range(2, 11):
            print(i)
    
#while loop
    i = 2
    
    while(i<=10):
        print(i)

    i += 1  

#for loop for string
simple_string = str('This is a simple string')

for element in simple_string:
    print(element, end=' ')
    
#nested loop nonsense
nested_loop = ['this', 'is', 'a', 'simple', 'string']

for nested_loop in nested_loop:
    
    count = 0
    while count < 3:
        print(nested_loop, end=' ')
     
        count = count + 1
    
    print()