import argparse
import imp
import os
import select_cuda
import time
import numpy as np
from extract_a import extract

args = argparse.ArgumentParser()
args.add_argument('start_line', type=int)
args.add_argument('--end', type=int, default=None)
args.add_argument('--cuda', type=str, default=None)

args=args.parse_args()

if args.cuda == None:
    cuda = None
else:
    cuda_str = args.cuda.split(',')
    cuda = [int(i) for i in cuda_str]

All_task = extract(args.start_line, args.end_line)
####################################

f = open('a.txt','r')
P = select_cuda.pool()

for line in All_task:
    while(P.select(select_list=cuda) == None):
        time.sleep(60)
    Current_gpu = P.select(select_list=cuda)[0]
    os.system('CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' nohup ' + line + ' &')
    print('Adding.....')
    print(time.ctime() + 'CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' ' + line)
    f_record = open('record_a.txt','a')
    f_record.write(time.ctime() + 'CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' ' + line + '\n')
    f_record.close()

    time.sleep(20)

f.close()