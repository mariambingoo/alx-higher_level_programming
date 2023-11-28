def fizzbuzz():
  for _ in range (1,101):
    if _ % 5 == 0 and _ % 3 == 0:
      print("FizzBuzz", end=" ")
    if _ % 3 == 0:
      print('fizz', end=" ")
    elif _ % 5 ==0:
      print ('buzz', end=" ")
    else:
      print(_ , end=" ")
 
