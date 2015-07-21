from cuisine_data import people_list

Chi_Mex = 0
Chi_Ind = 0
Ind_Mex = 0
dic = {}

for people in people_list:
    for preference in people:
        pref = preference
        if people[preference] == "likes":
            pref = True
        else:
            pref = False
        dic[preference] = pref
    if dic["Chinese"] and dic["Mexican"]:
        Chi_Mex += 1
    if dic["Chinese"] and dic["Indian"]:
        Chi_Ind += 1
    if dic["Indian"] and dic["Mexican"]:
        Ind_Mex += 1
        
print "Chinese and Mexican: {}".format(Chi_Mex)
print " Chinese and Indian: {}".format(Chi_Ind)
print " Indian and Mexican: {}".format(Ind_Mex)
