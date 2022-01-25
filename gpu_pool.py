from multiprocessing import current_process, Pool
import argparse
import subprocess
import os
import time

def run_single_GPU(task, GPU_list):
    p = current_process()._identity[0]
    task_str = 'CUDA_VISIBLE_DEVICES={} {}'.format(GPU_list[p-1], task)
    print('Start task: ' + task_str)
    # time.sleep(1)
    os.system(task_str)
    print('Finish task: ' + task)

if __name__ == '__main__':
    argps = argparse.ArgumentParser()
    argps.add_argument('--GPU', type=str, default='-1', help='Choose -1 to use all GPUs, other wise choose GPU indexes.')
    argps.add_argument('--All_task', type=str, default='a.txt', help='Each line in this file contains one task.')
    args = argps.parse_args()


    if args.GPU == '-1':
        All = subprocess.check_output('nvidia-smi --query-gpu=gpu_bus_id --format=csv,noheader', shell=True).decode('utf-8').strip('\n').split('\n')
        GPU_list = range(len(All))
    else:
        GPU_list = [int(i) for i in args.GPU.strip('\n').split(',')]

    print('Using GPU {}'.format(GPU_list))

    Tasks = open(args.All_task, 'r')
    for t in Tasks.readlines():
        print(t.strip())

    p = Pool(len(GPU_list))

    Tasks = open(args.All_task, 'r')
    for t in Tasks.readlines():
        p.apply_async(run_single_GPU, [t, GPU_list])

    p.close()
    p.join()
    
    Tasks.close()