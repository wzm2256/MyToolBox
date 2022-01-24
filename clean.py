# Cleaning the comment lines in latex file, remove multiple blank lines.
import argparse
import os
agsps = argparse.ArgumentParser()
agsps.add_argument('--old', type=str, required=True, help='Input file to be cleaned')
agsps.add_argument('--new', type=str, default='', help='Output file')
args = agsps.parse_args()

if args.new == '':
    new = os.path.dirname(args.old) + 'new_' + os.path.basename(args.old)
else:
    new = args.new

print('New file will be saved in {}'.format(new))

f_old = open(args.old, 'r', encoding='UTF-8')
f_new = open(new, 'w', encoding='UTF-8')

this_empty = True
for line in f_old.readlines():
    if line.strip(' ').strip('\t').startswith('%'):
        continue
    
    # if this_empty == False:
    #     f_new.write(line)
    #     if line == '\n':
    #         this_empty = True
    # else:
    #     if line == '\n':

    # else
    if line == '\n' and this_empty:
        pass
    else:
        f_new.write(line)
    if line == '\n':
        this_empty = True
    else:
        this_empty = False
    # elif this_empty == False:
    #     f_new.write(line)
    # elif 
    # this_empty = False
