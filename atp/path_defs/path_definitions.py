import os

class ATP_paths():

    def __init__(self):
        # check raw data archive path extant:
        self.atp_data_path = os.path.join('../..','raw_data','archive')
        assert os.path.exists(self.atp_data_path)

        # set read_data path for chunking later on:
        self.read_data_path = os.path.join('../..','raw_data','read_data')
        assert os.path.exists(self.read_data_path) 

        # check initial data file expected are extant:
        self.matches_data_path_full = os.path.join(self.atp_data_path, 'all_matches.csv')
        assert os.path.exists(self.matches_data_path_full)

    def get_read_data_path(self):
        return self.atp_data_path
    
    def get_matches_data_path_full(self):
        return self.matches_data_path_full
    
    def get_atp_data_path(self):
        return self.atp_data_path
