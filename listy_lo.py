if __name__ == "__main__":

    food = ['rice', 'beans']
    food.append('broccoli')
    
#time to mess this list up!
    carbs = ['bread', 'pizza']

    food.extend(carbs)
    
    print(food)

#now to slice...
first2items = food[0:2]

print(first2items)

#crying breakfast friends below
bad_breakfast = "eggs fruit orange_juice"

breakfast = bad_breakfast.split()

print(breakfast)