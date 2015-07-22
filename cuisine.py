from cuisine_data import people_list
# get stuff to not be hard-coded

def compute_cooccurence(people_list=people_list):
    """
    this function computes the co-occurence matrix
    :param people_list: list of people's cuisine preferences
    :return: the co-occerence matrix
    """

    Chi_Mex = 0
    Chi_Ind = 0
    Ind_Mex = 0
    dic = {}

    for people in people_list:
        for cuisine, preference in people.iteritems():
            dic[cuisine] = True if preference == "likes" else False

#change this stuff to make it more generic
        if dic["Chinese"] and dic["Mexican"]:
            Chi_Mex += 1
        if dic["Chinese"] and dic["Indian"]:
            Chi_Ind += 1
        if dic["Indian"] and dic["Mexican"]:
            Ind_Mex += 1

    print "Chinese and Mexican: {}".format(Chi_Mex)
    print " Chinese and Indian: {}".format(Chi_Ind)
    print " Indian and Mexican: {}".format(Ind_Mex)

    return Chi_Mex, Chi_Ind, Ind_Mex
