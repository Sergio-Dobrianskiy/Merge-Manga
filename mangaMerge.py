import os
import shutil
from natsort import natsorted, ns

manga_dir = r"D:\01 - Python\Manga"
en_dir = r"D:\01 - Python\Manga\en"
jp_dir = r"D:\01 - Python\Manga\jp"
output_dir = r"D:\01 - Python\Manga\output"

f_title = "Baby Steps"

# Changes jp file names
counter = 1
os.chdir(jp_dir)

jp_list = os.listdir(jp_dir)
jp_list = natsorted(jp_list, key=lambda y: y.lower())
for f in jp_list:
    f_name, f_ext = os.path.splitext(f)
    f_num = str(counter).zfill(3)
    new_name = '{}a-{}-jp{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)
    counter += 1

# Copies all renamed files from jp to output
for f in os.listdir(jp_dir):
    shutil.copy(f, output_dir)

# Changes en folder file names
counter = 1
os.chdir(en_dir)
en_list = os.listdir(en_dir)
en_list = natsorted(en_list, key=lambda y: y.lower())
for f in en_list:
    f_name, f_ext = os.path.splitext(f)
    f_num = str(counter).zfill(3)
    new_name = '{}b-{}-en{}'.format(f_num, f_title, f_ext)
    os.rename(f, new_name)
    counter += 1

# Copies all renamed files from en to output
for f in os.listdir(en_dir):
    shutil.copy(f, output_dir)