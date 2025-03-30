import os
from pathlib import Path


class BuildAppStructure:
    def __init__(self):
        self.home_path = Path.home()
        self.base_dir_name: str = "wbs-scrapiary"
        self.__complete_base_path = self.home_path.joinpath(
            self.home_path, self.base_dir_name
        )
        __mode: int = int(0o755)
        self.__mode = __mode
        self.__subdirectories: tuple = (
            "properly_app/modules",
            "properly_app/modules/onsite_docker",
            "databases/directly_databases",
            "user_files/user_pulled_files",
        )


    def make_inner_dirs(self, path) -> bool:
        try:
            os.makedirs(path, exist_ok=True, mode=self.__mode)
            print(f"Successfully created directory: {path}")
            return True
        except PermissionError:
            print(f"Permission denied: Cannot create directory {path}")
            return False
        except OSError as oe:
            print(f"Error creating directory {path}: {oe}")
            return False


    def create_dirs(self) -> list:
        basing_path = self.__complete_base_path
        if not basing_path.exists():
            os.chdir(self.home_path)
            os.mkdir(self.base_dir_name, mode=self.__mode)
        else:
            print(f"A directory named {self.base_dir_name} already exists! ")

        full_paths_list = [basing_path]
        for item in self.__subdirectories:
            path_as_str = basing_path.joinpath(basing_path, item)
            full_paths_list.append(path_as_str)

        for path_ in full_paths_list:
            self.make_inner_dirs(path_)

        return full_paths_list


    def output_app_structure(self) -> list:
        app_struct_list = sorted(Path(self.__complete_base_path).glob('**' + os.sep))
        print(app_struct_list)
        return app_struct_list


if __name__ == '__main__':
    build_app_struct = BuildAppStructure()
    build_app_struct.create_dirs()
    # path_list = build_app_struct.output_app_structure()
    # print(f"List of paths: {path_list}")


# folder_name = dir_name.replace(':', '').replace('.','')