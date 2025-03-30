import wbgapi as wbi
import pandas as pd
import pathlib

from datetime import datetime as dtm
from make_directory import BuildAppStructure


class WbgApiWorking:
    def __init__(self):
        self.app_structure = BuildAppStructure()
        self.paths_list = self.app_structure.output_app_structure(7)


    def get_directory_path(self):
        self.local_path = self.paths_list
        print(self.local_path)
        return self.local_path


    def create_dfr(self, db_pkg: str):
        db_pkg_ = db_pkg
        act_on_data = wbi.data.DataFrame(db_pkg_, time=range(2015, 2024), labels=True) \
            .round(decimals=1) \
            .sort_values('YR2023', ascending=False)

        return act_on_data


    def write_dfr(self, bspath: pathlib.PosixPath, filename: str, dataframe: pd.DataFrame):
        dfr_ = dataframe
        filename_ = bspath.joinpath(filename)
        with open(filename_, 'w') as file:
            file.write(dfr_.to_string())

        return file


    def create_indicators_list(self, indicat_in, bspath_01, fl_nm):
        fl_nm_ = bspath_01.joinpath(fl_nm)

        swap = {values: keys for keys, values in indicat_in.items()}
        swapped_indicats = pd.Series(swap)

        with open(fl_nm_, 'w') as onefile:
            onefile.write(swapped_indicats.to_string())

        return onefile


    def auto_naming(self):
        #db_info = wbi.series.list()
        dt_tm = dtm.now().strftime("%Y%m%d_%H%M%S")

        return dt_tm


if __name__ == '__main__':
    wbg_api_working = WbgApiWorking()

    #make_file = write_file(l_dir, naming, create_dataframe)
