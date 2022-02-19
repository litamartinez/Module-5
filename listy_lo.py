if __name__ == "__main__":

    food = ['rice', 'beans']
    food.append('broccoli')
    
#time to mess this list up! THIS ISS DONE
    carbs = ['bread', 'pizza']

    food.extend(carbs)
    
    print(food)

#now to slice... THIS IS DONE
first2items = food[0:2]

print(first2items)

#let's make some breakfast! THIS IS DONE
bad_breakfast = "eggs fruit orange_juice"

breakfast = bad_breakfast.split()

print(breakfast)

#using len on breakfast THISS IS DONE
print(len(breakfast))