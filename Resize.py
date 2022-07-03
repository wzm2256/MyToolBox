import PIL.Image as Image
import os
import argparse
import pdb

agsps = argparse.ArgumentParser()
agsps.add_argument('folder', type=str, help='Root folder for source files')

args = agsps.parse_args()

All_file = {}
for root, dirs, files in os.walk(args.folder):
    for f in files:
        file_i = os.path.join(root, f).replace('\\', '/')
        # All_file.append(file_i)
        size = os.path.getsize(file_i)
        All_file.update({file_i: size})
        # print(file_i + '\t' + str(size / 1000)  + 'K')



for i in All_file:
    img = Image.open(i)
    s = img.size
    # pdb.set_trace()
    new_img = img.resize((int(0.7 * s[0]), int(0.7 * s[1])))
    new_name = 'New_' + i
    if not os.path.isdir(os.path.dirname(new_name)):
        os.makedirs(os.path.dirname(new_name))
    new_img.save(new_name)