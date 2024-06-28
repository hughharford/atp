import os

from path_defs.path_definitions import ATP_paths

class Minors():
    
    def __init__(self):
        self.paths = ATP_paths()
        self.read_data_path = self.paths.get_read_data_path()

    def get_count_csvs(self, alt_path = None):
        '''defaults to: raw_data/read_data/'''
        if alt_path:
            path = alt_path
        else:
            path = self.read_data_path
        csv_files = []
        file_list = os.listdir(path)
        for i in file_list:
            if ".csv" in i:
                csv_files.append(os.path.join(path,i))
        return csv_files

    def check_environs(self):
        os.environ["our_new"] = ""
        envs = os.getenv("LOGNAME")
        # print(envs)
        assert envs == "hughharford"
        # if you get an error here, the notebook/code is not running 
        # in HSTH's expected place, and adjustments will be required.
        # print(os.environ)
        if envs == "hughharford":
            environment_running = 'laptop'
        else:
            environment_running = 0
        return environment_running

    def get_list_raw_data_files(self):
        '''counts no files & folders in /raw_data'''
        directory = '../../raw_data/' 
        onlyfiles = next(os.walk(directory))[2] #directory is your directory path as string
        return onlyfiles

