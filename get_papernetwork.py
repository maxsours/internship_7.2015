from paper_network_data import data

data_local = [
    {
        "bibcode": "2008PhDT.......169R", 
        "citation_count": 1, 
        "first_author": "Russcher, M. J.", 
        "read_count": 0.0, 
        "title": [
            "Direct photon measurement in proton-proton and deuteron-gold collisions"
        ], 
        "year": "2008"
    }, 
    {
        "bibcode": "2013arXiv1305.3460H", 
        "citation_count": 0, 
        "first_author": "Han, Hillary S. W.", 
        "read_count": 5.0, 
        "reference": [
            "2013arXiv1301.7177H"
        ], 
        "title": [
            "A bijection for tri-cellular maps"
        ], 
        "year": "2013"
    }, 
    {
        "bibcode": "2011MNRAS.413.2345H", 
        "citation_count": 8, 
        "first_author": "Hasan, Priya", 
        "read_count": 7.0, 
        "reference": [
            "1962AdA&A...1...47H", 
            "1964ARA&A...2..213B"
        ], 
        "title": [
            "Mass segregation in diverse environments"
        ], 
        "year": "2011"
    }, 
    {
        "bibcode": "1987sbge.proc..355F", 
        "citation_count": 2, 
        "first_author": "Fabian, A. C.", 
        "read_count": 0.0, 
        "title": [
            "Star formation in cooling flows."
        ], 
        "year": "1987"
    }, 
    {
        "bibcode": "1991ASPC...13...73M", 
        "citation_count": 6, 
        "first_author": "Myers, P. C.", 
        "read_count": 0.0, 
        "reference": [
            "1962AdA&A...1...47H", 
            "1964ARA&A...2..213B"
        ], 
        "title": [
            "The role of dense cores in isolated and cluster star formation."
        ], 
        "year": "1991"
    }, 
    {
        "bibcode": "1993sfgi.conf..324C", 
        "citation_count": 2, 
        "first_author": "Combes, F.", 
        "read_count": 0.0, 
        "title": [
            "External triggers of star formation."
        ], 
        "year": "1993"
    }, 
    {
        "bibcode": "1987PAICz..69..141K", 
        "citation_count": 0, 
        "first_author": "Kontizas, M.", 
        "read_count": 0.0, 
        "title": [
            "Density profiles of star clusters in the Magellanic Clouds."
        ], 
        "year": "1987"
    }
]
def get_bibref_data(solr_data):
    """
    This function gets a dictionary of bibcodes and references from the input data.
    """
    bibref_data = {}
    for paper in solr_data:
        if paper.get("reference") is not None:
            bibref_data[paper.get("bibcode")] = paper.get("reference")
    return bibref_data
    
def get_reference_unique_list(data_dict):
    """
    This function gets a list of each reference in the data dictionary.
    """
    reference_list = []
    
    for l in data_dict.values():
        for i in l:
            reference_list.append(i)
    reference_unique_list = list(set(reference_list))
    return reference_unique_list
    
def get_refdic_list(data_dict, ref_list):
    """
    This function gets a list of dictionaries with reference keys and boolean values given a list of total references and an original data dictionary.
    """
    refdic_list = []
    
    for l in data_dict.values():
        bool_dic = {k: False for k in ref_list}
        for i in l:
            for k in ref_list:
                if i is k:
                    bool_dic[i] = True
        refdic_list.append(bool_dic)
    return refdic_list
    
def get_pair_list(refdic_list):
    """
    From a list of dictionaries with reference keys and boolean values get a list of co-occurrance pairs.
    """
    pair_list = []
    for dic in refdic_list:
        for k1 in dic.keys():
            for k2 in dic.keys():
                if dic[k1] and dic[k2] and k1 is not k2:
                    pair_list.append("{} and {}".format(k1, k2))
    return pair_list
    
    #yay more functions here to make this data comprehensible
    
def get_papernetwork_nomatrix(solr_data):
    """
    This function gets the paper network and finds co-occurrance between references in papers in the input solr_data.
    """
    
    initial_data = {}
    for paper in solr_data:
        if paper.get("reference") is not None:
            initial_data[paper.get("bibcode")] = paper.get("reference")
    #assert initial_data == {'1991ASPC...13...73M': ['1962AdA&A...1...47H', '1964ARA&A...2..213B', '1979AJ.....84.1872J', '1979ApJS...41..743C', '1982VA.....26..159G', '1983A&A...128..279B', '1986ApJ...307..609H', '1988LicOB1111....1H', '1988Sci...242.1264G', '1989ApJ...340..823W', '1989ApJ...345L..79S', '1989BAAS...21R.712M', '1990PhDT.........4L', '1990moas.book..328M'],
                #'2011MNRAS.413.2345H': ['1962AJ.....67..471K', '1965ApJ...141..660W', '1968ArA.....5...45L', '1974VeBoc...2....1M', '1977Obs....97..129F', '1978AJ.....83..266F', '1982A&A...109..213L', '1986ApJ...310..613M', '1988MNRAS.234..831S', '1990AcASn..31...84Z', '1990ApJ...353..174S', '1991MNRAS.253..649T', '1992A&AS...94...73R', '1992AcApS..11..336P', '1992Natur.359..772H', '1994A&AS..105...15T', '1994AJ....108.1773J', '1995ARA&A..33..381F', '1995ApJ...454..151M', '1995JKAS...28..119S', '1997AJ....113..713D', '1997AJ....114..198C', '1998A&A...333..897R', '1998AJ....116..801P', '1998ApJ...492..540H', '1998MNRAS.295..691B', '1998gaas.book.....B', '1999A&A...349..825V', '1999A&AS..134..301C', '2000A&AS..144..451B', '2001AJ....121.2075M', '2002A&A...381..219D', '2002A&A...391..195G', '2002MNRAS.337..597D', '2002Sci...295...82K', '2003A&A...397..177B', '2003ApJ...592..975L', '2004A&A...416..137G', '2005A&A...437..483B', '2005A&A...437.1029D', '2005A&A...438.1163K', '2005Natur.438..332K', '2006A&A...445..567B', '2006A&A...446..121B', '2006A&A...459..489D', '2006A&A...460...83B', '2006AJ....131.1163S', '2006MNRAS.370..488B', '2007ApJ...655L..45M', '2007MNRAS.377.1301B', '2007MNRAS.377.1737P', '2007MNRAS.380.1141S', '2007MNRAS.380.1271P', '2007prpl.conf..149B', '2008A&A...488..211C', '2008AJ....135.1934S', '2008Ap&SS.318...25H', '2008ChJAA...8..362T', '2008gady.book.....B', '2009ApJ...700L..99A', '2009MNRAS.396.1864M', '2009MNRAS.397L..36G', '2010ARA&A..48..339B', '2010RSPTA.368..829V'],
                #'2013arXiv1305.3460H': ['2013arXiv1301.7177H']}
    reference_list = []
    for l in initial_data.values():
        for i in l:
            reference_list.append(i)
            
    #assert reference_list == ['1962AdA&A...1...47H', '1964ARA&A...2..213B', '1979AJ.....84.1872J', '1979ApJS...41..743C', '1982VA.....26..159G', '1983A&A...128..279B', '1986ApJ...307..609H', '1988LicOB1111....1H', '1988Sci...242.1264G', '1989ApJ...340..823W', '1989ApJ...345L..79S', '1989BAAS...21R.712M', '1990PhDT.........4L', '1990moas.book..328M', '1962AJ.....67..471K', '1965ApJ...141..660W', '1968ArA.....5...45L', '1974VeBoc...2....1M', '1977Obs....97..129F', '1978AJ.....83..266F', '1982A&A...109..213L', '1986ApJ...310..613M', '1988MNRAS.234..831S', '1990AcASn..31...84Z', '1990ApJ...353..174S', '1991MNRAS.253..649T', '1992A&AS...94...73R', '1992AcApS..11..336P', '1992Natur.359..772H', '1994A&AS..105...15T', '1994AJ....108.1773J', '1995ARA&A..33..381F', '1995ApJ...454..151M', '1995JKAS...28..119S', '1997AJ....113..713D', '1997AJ....114..198C', '1998A&A...333..897R', '1998AJ....116..801P', '1998ApJ...492..540H', '1998MNRAS.295..691B', '1998gaas.book.....B', '1999A&A...349..825V', '1999A&AS..134..301C', '2000A&AS..144..451B', '2001AJ....121.2075M', '2002A&A...381..219D', '2002A&A...391..195G', '2002MNRAS.337..597D', '2002Sci...295...82K', '2003A&A...397..177B', '2003ApJ...592..975L', '2004A&A...416..137G', '2005A&A...437..483B', '2005A&A...437.1029D', '2005A&A...438.1163K', '2005Natur.438..332K', '2006A&A...445..567B', '2006A&A...446..121B', '2006A&A...459..489D', '2006A&A...460...83B', '2006AJ....131.1163S', '2006MNRAS.370..488B', '2007ApJ...655L..45M', '2007MNRAS.377.1301B', '2007MNRAS.377.1737P', '2007MNRAS.380.1141S', '2007MNRAS.380.1271P', '2007prpl.conf..149B', '2008A&A...488..211C', '2008AJ....135.1934S', '2008Ap&SS.318...25H', '2008ChJAA...8..362T', '2008gady.book.....B', '2009ApJ...700L..99A', '2009MNRAS.396.1864M', '2009MNRAS.397L..36G', '2010ARA&A..48..339B', '2010RSPTA.368..829V', '2013arXiv1301.7177H']
    reference_unique_list = list(set(reference_list))
    #assert reference_unique_list == ['1965ApJ...141..660W', '1991MNRAS.253..649T', '2008AJ....135.1934S', '2002A&A...381..219D', '2007MNRAS.380.1271P', '2010RSPTA.368..829V', '1994AJ....108.1773J', '1974VeBoc...2....1M', '1992Natur.359..772H', '1986ApJ...310..613M', '2005A&A...438.1163K', '2006AJ....131.1163S', '2007ApJ...655L..45M', '2003ApJ...592..975L', '1962AdA&A...1...47H', '1983A&A...128..279B', '1995ARA&A..33..381F', '1997AJ....113..713D', '1990moas.book..328M', '2007MNRAS.380.1141S', '1986ApJ...307..609H', '2006A&A...445..567B', '1968ArA.....5...45L', '2002A&A...391..195G', '1992A&AS...94...73R', '1998ApJ...492..540H', '1995JKAS...28..119S', '2008ChJAA...8..362T', '2010ARA&A..48..339B', '2009ApJ...700L..99A', '1988Sci...242.1264G', '1982A&A...109..213L', '1962AJ.....67..471K', '2007MNRAS.377.1301B', '1964ARA&A...2..213B', '1998gaas.book.....B', '2008A&A...488..211C', '1995ApJ...454..151M', '2002MNRAS.337..597D', '2005Natur.438..332K', '1989ApJ...345L..79S', '1994A&AS..105...15T', '1990AcASn..31...84Z', '2013arXiv1301.7177H', '1988MNRAS.234..831S', '2008gady.book.....B', '1979AJ.....84.1872J', '1977Obs....97..129F', '2004A&A...416..137G', '1998MNRAS.295..691B', '2009MNRAS.396.1864M', '1998AJ....116..801P', '1990PhDT.........4L', '1979ApJS...41..743C', '2002Sci...295...82K', '2005A&A...437..483B', '2009MNRAS.397L..36G', '1997AJ....114..198C', '1982VA.....26..159G', '1988LicOB1111....1H', '1999A&A...349..825V', '2000A&AS..144..451B', '1989BAAS...21R.712M', '2006A&A...459..489D', '1978AJ.....83..266F', '1990ApJ...353..174S', '1998A&A...333..897R', '2006A&A...460...83B', '2003A&A...397..177B', '2007prpl.conf..149B', '2006A&A...446..121B', '2007MNRAS.377.1737P', '2008Ap&SS.318...25H', '2006MNRAS.370..488B', '1989ApJ...340..823W', '1992AcApS..11..336P', '2005A&A...437.1029D', '2001AJ....121.2075M', '1999A&AS..134..301C']
    ref_dic_list = []
    
    for l in initial_data.values():
        reference_bool_dic = {k: False for k in reference_unique_list}
        new_dic = get_bool(reference_bool_dic, l, reference_unique_list)
        ref_dic_list.append(new_dic)
    print "ref_dic_list", ref_dic_list
    
    pair_list = []
    for dic in ref_dic_list:
        for k1 in dic.keys():
            for k2 in dic.keys():
                if dic[k1] and dic[k2] and k1 is not k2:
                    pair_list.append("{} and {}".format(k1, k2))
        #assert pair_list.count('2007MNRAS.377.1737P and 2008A&A...488..211C') == 1
    print "pair_list", pair_list
    return pair_list
    
def get_bool(dic, list_, ref_list):
    """
    Given a dictionary with bibcode keys and boolean values (that all equal False at first), a list with references from one paper, and a list of total references, modify the bibcode keys and make the ones in the list equal to True.
    """
    for i in list_:
        for k in ref_list:
            if i is k:
                dic[i] = True
    return dic
    
def cooccurrance_count(co_list):
    """
    Given the list of co-occurrances and two objects, determine if those objects co-occurr.
    """
    print "Input two bibcodes: "
    ref1 = raw_input("[#1]: ")
    ref2 = raw_input("[#2]: ")
    return co_list.count("{} and {}".format(ref1, ref2))
    
#print "Input two bibcodes: "
#ref1 = raw_input("[#1]: ")
#ref2 = raw_input("[#2]: ")
print cooccurrance_count(get_papernetwork_nomatrix(data))

#"1962AdA&A...1...47H", 
#"1964ARA&A...2..213B"

