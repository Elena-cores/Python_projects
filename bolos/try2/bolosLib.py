class NumberOfRounds(Exception):
    pass

def deserialize(gameRun):
    result = gameRun.split(" ")
    result = map(lambda s: s.split('-'), result) # mapeo de función split 
    result = [[0 if x == "" else int(x) for x in s] for s in result] # list comprehension 
    return result


def evaluation(run):
    score = 0
    data = deserialize(run) 
    if len(data) != 10: raise NumberOfRounds("Invalid number of rounds")
    for i in range(len(data)):
        frame = data[i]
        if i != 9:
            if frame[0] == 10:
                if i<= 7 and data[i+1][0] == 10:     # next round is also strike
                        score += 20 + data[i+2][0]
                else:
                    score += 10 + data[i+1][0] + data[i+1][1]   # strike
            elif frame[0] + frame[1] == 10:   # spare 
                score += 10 + data[i+1][0]  
            else:
                score +=  frame[0] + frame[1] # open frame 
        else: 
            if frame[0] == 10:
                score += 10 + frame[1] + frame[2]
            elif frame[0] + frame[1] == 10:
                score += 10 + frame[2]
            else:
                score += frame[0] + frame[1] 
    return score


