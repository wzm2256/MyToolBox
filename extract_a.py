import numpy as np
import os

def extract(start_line, end_line=None, record=True):
    if end_line == None:
        end_line = np.inf

    #####################################
    # Record Task
    #####################################
    All_task = []
    f = open('a.txt','r')
    f_record = open('record_a.txt','w')
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
        if line.strip().startswith('#'):
            continue
        print(line.strip())
        f_record.write(line)
        All_task.append(line.strip())
    
    f_record.write('\n')
    f_record.close()
    f.close()
    return All_task