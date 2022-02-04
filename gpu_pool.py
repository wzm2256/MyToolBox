from multiprocessing import current_process, Pool
import argparse
import subprocess
import os
import time
from extract_a import extract
def run_single_GPU(task, GPU_list):
    p = current_process()._identity[0]
    ### In Linux
    if os.name == 'nt':
        prefix = 'set CUDA_VISIBLE_DEVICES={} &'.format(GPU_list[p-1])
    else:
        prefix = 'CUDA_VISIBLE_DEVICES={}'.format(GPU_list[p-1])

    task_str = prefix + ' {}'.format(task)
    print('Start task: ' + task_str)
    # time.sleep(1)
    os.system(task_str)
    print('Finish task: ' + task)

if __name__ == '__main__':
    argps = argparse.ArgumentParser()
    argps.add_argument('--GPU', type=str, default='-1', help='Choose -1 to use all GPUs, other wise choose GPU indexes.')
    argps.add_argument('--start', type=int, default=0)
    argps.add_argument('--end', type=int, default=None)
    args = argps.parse_args()

    if args.GPU == '-1':
        All = subprocess.check_output('nvidia-smi --query-gpu=gpu_bus_id --format=csv,noheader', shell=True).decode('utf-8').strip('\n').split('\n')
        GPU_list = range(len(All))
    else:
        GPU_list = [int(i) for i in args.GPU.strip('\n').split(',')]

    print('Using GPU {}'.format(GPU_list))
    p = Pool(len(GPU_list))

    All_task = extract(args.start, args.end)
    for t in All_task:
        p.apply_async(run_single_GPU, [t, GPU_list])

    p.close()
    p.join()