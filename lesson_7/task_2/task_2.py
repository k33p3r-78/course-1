import json

starter = {}
folders = {}
with open('config_2.yaml', mode='rt', encoding='UTF-8') as f:
    for line in f:
        line = line.rstrip()
        if not line.startswith(' ') and line.endswith(':'):
            path_arr = [line]
        else:
            path_arr = line.split('  ')
            path_arr[-1] = path_arr[-1][2:]

        path_name, path_level = path_arr[-1], len(path_arr)
        if path_name.endswith(':'):
            folder_name = path_name[:-1]
            folders[path_level] = folder_name
            print(path_level)
        else:
            starter_cursor = starter
            for curr_level in range(1, path_level):
                if folders[curr_level] not in starter_cursor:
                    starter_cursor[folders[curr_level]] = {}
                    starter_cursor = starter_cursor[folders[curr_level]]
                else:
                    starter_cursor[folders[curr_level]]
        
print(json.dumps(starter, indent=4))

        # if len(path_arr) in file_dict:
            # file_dict[len(path_arr)].append(path_arr[-1])
        # else:
            # file_dict[len(path_arr)] = [path_arr[-1], ]




