import os

for path, dirs, files in os.walk("."):
  for file in files:
    os.rename(path + "/" + file, path + "/" + file.replace("~","-"))
    
