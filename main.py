# making board
playboard = [
    [0,0,0 ,7,0,0, 0,0,0], 
    [0,0,9 ,0,8,4, 0,7,5], 
    [8,0,3 ,0,0,0, 0,2,0],

    [2,0,1 ,0,4,0, 0,0,3],
    [0,0,0 ,9,5,0, 0,4,0],
    [0,0,0 ,3,0,0, 0,0,1],

    [0,8,2 ,4,0,0, 0,0,0],
    [0,0,7 ,8,0,2, 0,0,0],
    [0,1,0 ,0,9,0, 7,0,0]
    ]

# making variables of each box
box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9 = [], [], [], [], [], [], [], [], []
row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9 = [], [], [], [], [], [], [], [], []

# making 3*3 square
def new_box():
    for coulam in range(9):
        for row  in range(9):
            if coulam //3 == 0 and row //3 == 0:box_1.append(playboard[coulam][row])
            elif coulam //3 == 0 and row //3 == 1:box_2.append(playboard[coulam][row])
            elif coulam //3 == 0 and row //3 == 2:box_3.append(playboard[coulam][row])
            elif coulam //3 == 1 and row //3 == 0:box_4.append(playboard[coulam][row])
            elif coulam //3 == 1 and row //3 == 1:box_5.append(playboard[coulam][row])
            elif coulam //3 == 1 and row //3 == 2:box_6.append(playboard[coulam][row])
            elif coulam //3 == 2 and row //3 == 0:box_7.append(playboard[coulam][row])
            elif coulam //3 == 2 and row //3 == 1:box_8.append(playboard[coulam][row])
            elif coulam //3 == 2 and row //3 == 2:box_9.append(playboard[coulam][row])


# creating function which find out where a particular number is in which box
def finding_box(coulam, row):
    new_box()
    if coulam //3 == 0 and row //3 == 0:return box_1
    elif coulam //3 == 0 and row //3 == 1:return box_2
    elif coulam //3 == 0 and row //3 == 2:return box_3
    elif coulam //3 == 1 and row //3 == 0:return box_4
    elif coulam //3 == 1 and row //3 == 1:return box_5
    elif coulam //3 == 1 and row //3 == 2:return box_6
    elif coulam //3 == 2 and row //3 == 0:return box_7
    elif coulam //3 == 2 and row //3 == 1:return box_8
    elif coulam //3 == 2 and row //3 == 2:return box_9


# creating a function which will find out where a particular number is there in which row
def finding_row(index_number):
    row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9 = [], [], [], [], [], [], [], [], []
    for coulam in range(9):
        for row  in range(9):
            if row == index_number:
                row_1.append(playboard[coulam][row])
    return row_1


# returning a list of postion of a particular box when it's called  
def box_position(selected_box):
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = [], [], [], [], [], [], [], [], []
    for j in range(9):
        for i in range(9):
            if playboard[j][i] == 0:
                if j //3 == 0 and i //3 == 0:box1.append([j,i])
                elif j //3 == 0 and i //3 == 1:box2.append([j,i])
                elif j //3 == 0 and i //3 == 2:box3.append([j,i])
                elif j //3 == 1 and i //3 == 0:box4.append([j,i])
                elif j //3 == 1 and i //3 == 1:box5.append([j,i])
                elif j //3 == 1 and i //3 == 2:box6.append([j,i])
                elif j //3 == 2 and i //3 == 0:box7.append([j,i])
                elif j //3 == 2 and i //3 == 1:box8.append([j,i])
                elif j //3 == 2 and i //3 == 2:box9.append([j,i])
    if selected_box == box_1: 
        return box1    
    elif selected_box == box_2: 
        return box2
    elif selected_box == box_3: 
        return box3
    elif selected_box == box_4: 
        return box4
    elif selected_box == box_5: 
        return box5
    elif selected_box == box_6: 
        return box6
    elif selected_box == box_7: 
        return box7
    elif selected_box == box_8: 
        return box8
    elif selected_box == box_9: 
        return box9

# creating a list of possible solution which will help 
possible_solution = []
for i in range(9):
    possible_solution.append([])
    for j in range(9):
        if playboard[i][j] != 0:
            possible_solution[i].append([playboard[i][j]])
        else:
            possible_solution[i].append([])

# method 1: in this method it will find which a number which is possible in that particular box through row's , coluam's and box's
def method1():
    
    coulams_while_finding = 0
    # coulams_while_finding = 9 loop will break
    while coulams_while_finding != 9:
        starting = 0
        # count the number 0 and save it in a varible called count_of_0
        count_of_0 = playboard[coulams_while_finding].count(0)
        # iterating through how many 0's are there in coulam 
        for iteration_of_count_of_0 in range(count_of_0):
            # creating a varible missing_value which will the index of 0 in playboard 
            missing_value = playboard[coulams_while_finding].index(0, starting)
            # creating a list of number through 1 to 9

            all_numbers = [i for i in range(1,10)]  
            # creating a empty list
            possible_solution_of_particular_number = []
            # finding a number which is not in box, row, coluam and excluded from all_number 
            for i in all_numbers:
                if i not in finding_box(coulams_while_finding,missing_value):
                    if  i not in finding_row(missing_value):
                        if  i not in playboard[coulams_while_finding]:
                            #if i not in possible_solution[coulams_while_finding][missing_value]:
                            possible_solution_of_particular_number.append(i)
            # positioning all the possiblites that into same box
            possible_solution[coulams_while_finding][missing_value].extend(possible_solution_of_particular_number)
            if len(possible_solution_of_particular_number) == 1:
                playboard[coulams_while_finding][missing_value] = possible_solution_of_particular_number[0]
            # else add 1 to starting varible through which it will not loop forever 
            else:
                starting = missing_value+1
        else:
            coulams_while_finding += 1





    # finding_number from 1 to 9
    for finding_number in range(1,10):
        position = []
        # making a list of every box through which we can reamove a box if there is the finding number
        boxs = [box_1,box_2,box_3,box_4,box_5,box_6,box_7,box_8,box_9]
        # looping through every coluam 
        for coluam in range(9):
            # making try and expect block if the finding_number is not in that coluam
            try:
                # finding the index of the finding_number 
                number = playboard[coluam].index(finding_number)
                # removing box if number is there in that box
                boxs.remove(finding_box(coluam, number))
                # geting the postion of finding_number
                position.append([coluam,number])
        
            except Exception as e:
                continue
        
        
        all_box = []
        reject_list= []
        # This will make a list of list and append that in all box function 
        for box in boxs:
            function = box_position(box)
            all_box.append(function)

        # it will remove poistion of the from all box where there is finding number in row or coluam      
        for finded_i_and_j in position:
            i = finded_i_and_j[0]
            j = finded_i_and_j[1]
            for one_all_boxs in all_box:
                index = 0
                last_postion = one_all_boxs[-1]
                while True:
                    one_all_box = one_all_boxs[index]
                    possible_i = one_all_box[0]
                    possible_j = one_all_box[1]
                    if i == possible_i or j == possible_j:
                        one_all_boxs.pop(index)
                    else :
                        reject_list.append(one_all_box)
                        index  +=1
                    if one_all_box == last_postion:
                        break
        # This will check if there is only one possiblity of finding number in one box  
        for checking_one_box in all_box:
            if len(checking_one_box) ==1:
                for one_box in checking_one_box:
                    j = one_box[0]
                    i = one_box[1]
                    playboard[j][i] = finding_number
                    possible_solution[j][i] = [finding_number]
            else:
                for ij in checking_one_box:
                    j = ij[0]
                    i = ij[1]
                    possible_solution[j][i].append(finding_number)  
def last_step():
    for i in playboard:
        while 0 in i:
            method1()
    print('  - - -   - - -   - - -  ')
    for i in range(9):
        for j in range(9):
            if j % 3 == 2:
                print(playboard[i][j],"| ",end="")
            elif j == 0:
                print('|',playboard[i][j] , end=' ') 
            else:
                print(playboard[i][j],end=" ")
        if i % 3 == 2:
            print("\n  - - -   - - -   - - -  ") 
        else:print('\n')
    
if __name__ == '__main__':
    last_step()


