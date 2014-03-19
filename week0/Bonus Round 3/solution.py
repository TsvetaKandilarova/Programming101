def final_position (commands, A, B):
    position = 0
    #print ("start")

    if len (commands) < 1 or len (commands) > 50:
        return False

    if B > 50 or A > 50 or A < 1 or B < 1:
        return False

    for i in range(len(commands)):
        if commands[i] == 'L':
            if position > (-A):
                position -= 1

        elif commands[i] == 'R':
            if position < B:
                position += 1

        else:
            return False

        #print (str(position) + "->")

    return position

