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