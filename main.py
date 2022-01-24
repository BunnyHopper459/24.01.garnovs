text=input("Ievadi tekstu: ")
x = text.count("o"),text.count("O")
if x > 0:
  print(text.replace("o","%"),text.replace("O","%"))
elif x == 0:
  print("No letter was found")
