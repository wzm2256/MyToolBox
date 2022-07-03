import os
import shutil
import argparse

argps = argparse.ArgumentParser()
argps.add_argument('folder', type=str)

args = argps.parse_args()


All = os.listdir(args.folder)


for i in All:
    name_seg = i.split('.')
    new_name = ''
    for s in range(len(name_seg)-1):
        new_name += name_seg[s]
        new_name += '_'
    new_name += '.'
    new_name += name_seg[-1]
    print(i)
    print(new_name)

    shutil.move(os.path.join(args.folder, i), os.path.join(args.folder, new_name))
# All_file
