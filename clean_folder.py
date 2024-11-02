import re
import argparse
import os   
from pathlib import Path
import pdb
import shutil

from multiprocessing import Pool

def find_bracketed_strings(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        text = f.read()
        # Find all strings between { and }
        pattern = r'{([^{}]*?)}'
        matches = re.findall(pattern, text)
        return matches



def check_file(args):
    i, t = args
    if str(Path(t)).startswith(str(Path(i)) + '.') or str(Path(t)) == str(Path(i)):
        return Path(t)
    return None

if __name__ == '__main__':

    agsps = argparse.ArgumentParser()
    agsps.add_argument('--file', type=str, required=True, help='Input main_tex files, separate with "," ')
    agsps.add_argument('--folder', type=str, required=True, help='Root folder for source files')

    args = agsps.parse_args()

    All_latex = args.file.strip().split(',')

    Collect_all = []
    for i in All_latex:
        Collect_all += find_bracketed_strings(i)


    All_file = []
    for root, dirs, files in os.walk(args.folder):
        for f in files:
            file_i = os.path.join(root, f)
            All_file.append(file_i)



    target_file = []
    with Pool() as pool:
        for i in Collect_all:
            results = pool.map_async(check_file, [(i, t) for t in All_file])
            matches = [r for r in results.get() if r is not None]
            target_file.extend(matches)


    Target_file = list(set(target_file))
    print('Found {} files in tex files:'.format(len(Target_file)))
    for i in Target_file:
        print(str(i))

    for i in Target_file:
        new_name = os.path.join('Clean_package', i)
        if not os.path.isdir(os.path.dirname(new_name)):
            os.makedirs(os.path.dirname(new_name))
        shutil.copy(i, new_name)

    print('Done!')

