f = open("test.txt", 'r').read()
f = f.replace("\n", ' ').split()


txt = "English French Italian Spanish German Dutch Polish Russian Bulgarian Greek"
txt = txt.split()

print(sorted(txt))

