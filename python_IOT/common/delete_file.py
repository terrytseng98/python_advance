import os

print(os.listdir())
file=input("Input Remove File name:")
os.remove(file)
print(os.listdir())