import argparse
import os
import select_cuda
import time
import numpy as np

args = argparse.ArgumentParser()
args.add_argument('start_line', type=int)
args.add_argument('--end', type=int, default=None)
args.add_argument('--cuda', type=str, default=None)

args=args.parse_args()

if args.cuda == None:
    cuda = None
else:
    cuda_str = args.cuda.strip().split(',')
    cuda = [int(i) for i in cuda_str]

if args.end == None:
    end_line = np.inf
else:
    end_line = args.end
start_line = args.start_line

#####################################
# Record Task
#####################################

f = open('a.txt','r')
f_record = open('record_a.txt','a')
pid = os.getpid()
print('pid: ', pid)
f_record.write('pid: '+str(pid) + '\n')
i = 0
print('Task List:\n')
f_record.write('Task List:\n')

for line in f.readlines():
    i += 1
    if i < start_line:
        continue
    if i > end_line:
        continue
    print(line)
    f_record.write(line)

f_record.write('\n')
f_record.close()
f.close()

####################################

f = open('a.txt','r')
P = select_cuda.pool()

i = 0
for line in f.readlines():
    i += 1
    if i < start_line:
        continue
    if i > end_line:
        continue

    
    while(P.select(select_list=cuda) == None):
        time.sleep(60)
    Current_gpu = P.select(select_list=cuda)[0]
    os.system('CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' nohup ' + line.strip() + ' &')
    print('Adding.....')
    print(time.ctime() + 'CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' ' + line.strip())
    f_record = open('record_a.txt','a')
    f_record.write(time.ctime() + 'CUDA_VISIBLE_DEVICES=' + str(Current_gpu) + ' ' + line.strip() + '\n')
    f_record.close()

    time.sleep(20)

f.close()