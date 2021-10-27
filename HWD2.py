# EX1
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def placeList(place):
    if place.lower()<= "  ":
        return False
    else:
        return True
    
newPlaceList=list(filter(placeList,places))
print(newPlaceList)

# EX2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def authorNames():
    
    author.sort(key=lambda a: a.split()[1])
    print(author)

authorNames()

# EX3
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angeles",44),("Miami",29)]


tempsF= list(map(lambda x,y: (y*9)/5+32,places ))
print(tempsF)

# EX4
def fibNums(num):
    # Set base case for recusive function
    if num <= 0:
        print("Iteration 0 : 1")
        return num
    else:
        print(f"Iteration {num} : ({num -2})")
        return(fibNums(num - 1) + fibNums(n-2))
    
fibNums(5)