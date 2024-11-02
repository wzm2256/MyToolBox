import argparse
import os
import shutil

agsps = argparse.ArgumentParser()
agsps.add_argument('--file', type=str, default=None, help='Input main_tex files, separate with ","')
agsps.add_argument('--folder', type=str, default=None, help='Root folder for tex files')

args = agsps.parse_args()

if args.folder is None:
    pwd = '.'
else:
    pwd = args.folder

if args.file is None:
    All_latex = [i for i in os.listdir(pwd) if i.endswith('.tex')]
else:
    All_latex = args.file.strip().split(',')

New_package = os.path.join(pwd, 'Clean_package')
if not os.path.isdir(New_package):
    os.makedirs(New_package)

All_latex_path = [os.path.join(pwd, i) for i in All_latex]
All_new_latex_path = [os.path.join(New_package, i) for i in All_latex]
All_new_tex = ','.join(All_new_latex_path)


print('Cleaning tex files:')
print(All_latex)

for i, j in zip(All_latex_path, All_new_latex_path):
    os.system('python -m clean_tex --old {} --new {}'.format(i, j))

os.system('python -m clean_folder --file {} --folder {}'.format(All_new_tex, pwd))
