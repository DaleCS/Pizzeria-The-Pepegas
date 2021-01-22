def calculateScore(pizza, freq):
  score = 0
  for ingredient in pizza["ingredients"]:
    score += freq[ingredient]
  return score


def solve():
  with open('a_example.txt') as f:
    freq = {}
    info = []
    pizzaObjects = []
    lines = f.readlines()
    counter = 0
    for line in lines:
      pizzaObj = {
        "id": 0,
        "numIngredients":0,
        "ingredients":[],
        "uniqueScore": 0
      }


      # if first line
      if counter == 0:
        info = line.split(' ')
      else:
        pizza = [x.strip() for x in line.split(' ')]
        pizzaObj["numIngredients"] = pizza[0]
        pizzaObj["ingredients"] = pizza[1:]
        pizzaObj["id"] = counter - 1
        pizzaObjects.append(pizzaObj)
        # print(pizza)
        numIngredients = pizza[0]
        for i in range(1, int(numIngredients) + 1):
          freq[pizza[i].strip()] = freq.get(pizza[i], 0) + 1

      counter += 1

    # print(freq)


    for obj in pizzaObjects:
      obj["uniqueScore"] = calculateScore(obj, freq)
      # print(obj)
  newlist = sorted(pizzaObjects, key=lambda x: x["uniqueScore"], reverse=False)

  for obj in newlist:
    print(obj)



solve()

# Mama Mia Mama Mia Mama Mia Mama Mia, I be makin' fkin dough at the pizzeria