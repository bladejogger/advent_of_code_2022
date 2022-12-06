FIN = "signal_stream.txt"

def main():
    sop_flag = False
    sop_recvd = 0
    sop_marker = []

    with open(FIN) as fin:
        line = fin.readline()
        print(f"{line}")
        for elem in line:
            sop_recvd += 1
            sop_marker.append(elem)
            if len(sop_marker) > 4:
                sop_marker.pop(0)
                # convert list to set as a dirty unique check
                if len(set(sop_marker)) == 4:
                    sop_flag = True
                    break

    if sop_flag:
        print(f"ANSWER: {sop_recvd}")
        print(f"marker: {sop_marker}")


if __name__ == "__main__":
    main()
