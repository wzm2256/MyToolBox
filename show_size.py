import os
import argparse

agsps = argparse.ArgumentParser()
# agsps.add_argument('--file', type=str, required=True, help='Input main_tex files, separate with "," ')
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

All_file = sorted(All_file.items(), key = lambda x:x[1], reverse = True)

for i in All_file:
    print(i[0], i[1]/1000)
# print(All_file)
