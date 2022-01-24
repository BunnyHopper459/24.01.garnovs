text=input("Ievadi tekstu: ")
x = int(text.count("o")+text.count("O"))
if x > 0:
  text=text.replace("o","%")
  text=text.replace("O","%")
  print(text)
elif x == 0:
  print("Burts nav atrasts!")
