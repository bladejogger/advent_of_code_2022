FIN = "rps_strategy.txt"

WIN_PTS = 6
TIE_PTS = 3
LOS_PTS = 0

A_X_PTS = 1 # rock
B_Y_PTS = 2 # paper
C_Z_PTS = 3 # scissor

def main():
    with open(FIN) as fin:
        total_pts = 0
        round_pts = 0

    # first column is what opponent plays
    # secon column is what outcome should be
        line = fin.readline().split()
        while line:
            if line[0] == 'A': # enemy rock
                if line[1] == 'X': # lose
                    round_pts += LOS_PTS
                    round_pts += C_Z_PTS
                elif line[1] == 'Y': # draw
                    round_pts += TIE_PTS
                    round_pts += A_X_PTS
                elif line[1] == 'Z': # win
                    round_pts += WIN_PTS
                    round_pts += B_Y_PTS
            elif line[0] == 'B': # enemy paper
                if line[1] == 'X': # lose
                    round_pts += LOS_PTS
                    round_pts += A_X_PTS
                elif line[1] == 'Y': # draw 
                    round_pts += TIE_PTS
                    round_pts += B_Y_PTS
                elif line[1] == 'Z': # win 
                    round_pts += WIN_PTS
                    round_pts += C_Z_PTS
            elif line[0] == 'C': # enemy scissors
                if line[1] == 'X': # lose 
                    round_pts += LOS_PTS
                    round_pts += B_Y_PTS
                elif line[1] == 'Y': # draw
                    round_pts += TIE_PTS
                    round_pts += C_Z_PTS
                elif line[1] == 'Z': # win 
                    round_pts += WIN_PTS
                    round_pts += A_X_PTS
            else:
                print("hella error brah")

            total_pts += round_pts
            round_pts = 0
            line = fin.readline().split()

        print(f"total score if following decrypted strat guide: {total_pts}")


if __name__ == "__main__":
    main()
