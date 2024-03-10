import os
from natsort import os_sorted


def rename_files_in_directory(directory):
    file_list = os_sorted(os.listdir(directory))
    ctr = 0
    for file in file_list:
        filename_split = os.path.splitext(file)
        if not filename_split[1] in [".ini"]:
            ctr += 1
            if filename_split[0] != str(ctr):
                file_path = os.path.join(directory, file)
                new_file_name = str(ctr) + filename_split[1]
                new_file_path = os.path.join(directory, new_file_name)
                os.rename(file_path, new_file_path)


root_directory = (
    r"D:\Users\smail\Downloads\sow9_obs_3\sow9_obs_3\Linux_OBS\720_1280\720_1280"
)
rename_files_in_directory(root_directory)
