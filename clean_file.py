# Copy used file in latex files to a new folder
import argparse
import os
import re
import pdb
import shutil

def extact_fname(root, tex_file):
    Collect = []
    pattern = '{' + root
    for line in tex_file.readlines():
        out = re.search(pattern, line)
        if out is None:
            continue
        else:
            ind = out.span()
        findstr = line[ind[0]: -1]

        end = re.search('}', findstr).span()[0]
        findstr1 = findstr[1:end]
        Collect.append(findstr1)
    return Collect



agsps = argparse.ArgumentParser()
agsps.add_argument('--file', type=str, required=True, help='Input main_tex files, separate with "," ')
agsps.add_argument('--folder', type=str, required=True, help='Root folder for source files')

args = agsps.parse_args()


All_latex = args.file.strip().split(',')

Collect_all = []
for i in All_latex:
    f = open(i, 'r', encoding='UTF-8')
    Collect_all += extact_fname(args.folder, f)


print('Found {} files in tex files:'.format(len(Collect_all)))
# for i in Collect_all:
#     print(i)

All_file = []
for root, dirs, files in os.walk(args.folder):
    for f in files:
        file_i = os.path.join(root, f).replace('\\', '/')
        All_file.append(file_i)


target_file = []

for i in Collect_all:
    Flag = 0
    for t in All_file:
        if re.search(i + '\.', t) != None or i == t:
            # pdb.set_trace()
            # print(i + '\t' + t)
            Flag = 1
            target_file.append(t)
            break
    if Flag == 0:
        raise ValueError('File' + i + ' not found!')

print('------------')
print('Found {} files in folders:'.format(len(target_file)))


for i in target_file:
    new_name = 'New_'+i
    if not os.path.isdir(os.path.dirname(new_name)):
        os.makedirs(os.path.dirname(new_name))
    shutil.copy(i, 'New_'+i)

print('Done!')
