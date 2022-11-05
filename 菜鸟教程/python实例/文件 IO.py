with open("text.txt", "w") as f1:
    f1.write("哎呦喂")

with open("text.txt", "r") as f2:
    print(f2.read())
