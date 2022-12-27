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

    total = 0
    for k,v in dict_syst.items():
        if v < 100000:
            print(f"{k} : {v}")
            total += v
    print(total)

if __name__ == "__main__":
    main()
