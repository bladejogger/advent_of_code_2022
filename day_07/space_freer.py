FIN = "file_structure.txt"

def main():
    filesystem = []
    dict_syst = dict()

    with open(FIN) as fin:
        line = fin.readline().split()
        while line:
            if line[1] == 'cd':
                if line[2] == "..":
                    filesystem.pop()
                else:
                    filesystem.append(line[2])
                    # '[1:0]' like this cuts off the extra '/' at the start
                    if not "/".join(filesystem)[1:] in dict_syst.keys():
                        dict_syst["/".join(filesystem)[1:]] = 0
            elif line[0].isnumeric():
                current_dir = "/".join(filesystem)[1:]
                dict_syst[current_dir] += int(line[0])
                # add the current directory size to all of the earlier path entries
                while current_dir:
                    former_path_pieces = current_dir.split("/")
                    current_dir = "/".join(former_path_pieces[:-1])
                    if not current_dir in dict_syst.keys():
                        dict_syst[current_dir] = 0
                    dict_syst[current_dir] += int(line[0])

            line = fin.readline().split()

    which_dir = []
    total_n_use = dict_syst[""]
    # 70,000,000
    total_space = 70000000
    # 30,000,000
    total_need = 30000000
    free_space = total_space - total_n_use
    still_need = total_need - free_space
    #print(f"total : {total_space:,}")
    #print(f"in use: {total_n_use:,}")
    #print(f"free  : {free_space:,}")
    #print(f"needed: {total_need:,}")
    #print(f"remain: {still_need:,}")
    total = 0
    for k,v in dict_syst.items():
        if v > still_need:
            which_dir.append((k, v))
    answer = sorted(which_dir, key=lambda space:space[1])
    print(f"{answer[0]}")
    
if __name__ == "__main__":
    main()
