if __name__ == "__main__":

    food = ['rice', 'beans']
    food.append('broccoli')
    
#time to mess up this list!
    carbs = ['bread', 'pizza']

    food.extend(carbs)
    
    print(food)

#now to slice... 
first2items = food[0:2]

print(first2items)

#let's make some breakfast! 
bad_breakfast = "eggs fruit orange_juice"

breakfast = bad_breakfast.split()

print(breakfast)

#using len on breakfast 
print(len(breakfast))

#prompt for floating point value -_-

numbers=[]
numbers_input=0

while numbers_input!="stop":
    #try:
        numbers_input=input("Enter a floating value. Otherwise, type STOP.")
        if numbers_input=="stop":

            print("All done!")
            print(f"You entered:{numbers}")
    #except:
    #        print("Oops, try again with a floating value (e.g. a real number with a decimal point):")
            break
    
        numbers.append(float(numbers_input))
    
print(numbers)

#second part with results
numbers_average = sum(numbers) / len(numbers)

print("In case you were wondering...")

print(f"The minimum value you entered is: {min(numbers)}")

print(f"The maximum value you entered is: {max(numbers)}")

print(f"The average value of what you entered is: {numbers_average}")
