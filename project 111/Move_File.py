import os
import shutil

from_dir = "C:/Users/Hai/Downloads"
to_dir = "C:/Users/Hai/Desktop"

list_of_Doc = os.listdir(from_dir)
print(list_of_Doc)

for Doc_name in list_of_Doc:
    name,extension = os.path.splitext(Doc_name)
   