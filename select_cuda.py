import subprocess

class pool:
    # def __init__(self, CudaList=None, PoolSize=None):
    def __init__(self):
        A = subprocess.check_output('nvidia-smi --query-gpu=gpu_bus_id --format=csv,noheader', shell=True)
        self.All = A.decode('utf-8').strip('\n').split('\n')
        # self.CudaList = CudaList
        # self.PoolSize = PoolSize
    def select(self, select_num=1, select_list=None):
        current = subprocess.check_output('nvidia-smi --query-compute-apps=gpu_bus_id --format=csv,noheader', shell=True)
        C_list = current.decode('utf-8').strip('\n').split('\n')

        Index_All = list(range(len(self.All)))
        Index_used = [i for i in range(len(self.All)) if self.All[i] in C_list]
        Index_have = list(set(Index_All) - set(Index_used))


        
        if select_list == None:
            Want_list = Index_All
        else:
            Want_list = select_list

        Pool_set = set(Want_list).intersection(set(Index_have))

        if len(Pool_set) < select_num:
            return None
        else:
            return list(Pool_set)[:select_num]


        # if len(list(set(self.All) - set(C_list))) < select_num:
        #     return None
        #     else:
        #         Select_name = list(set(self.All) - set(C_list))[:select_num]
        #         return [i for i in range(len(self.All)) if self.All[i] in Select_name]
        # else:
        #     if select_num != len(select_list):
        #         return None
        #     else:

