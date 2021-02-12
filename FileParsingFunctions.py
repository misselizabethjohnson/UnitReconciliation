def open_and_parse_file(fileName):
    '''
    Returns a tuple of relevant info for Unit Reconciliation. 

            Parameters:
                    fileName (str): name of file inside cwd
            Returns:
                    d0Data (list): A list of initial account data, i.e.
                        ['APPL 20', 'Cash 100.10', 'GOOG 30.75']
                    transactions (list): A list of transactions, i.e. 
                        ['APPL BUY 1 100.10', 'GOOG SELL 11.5 22']
                    d1Data (list): A list of final reported account data, 
                        i.e. ['APPL 300', 'TD 33.6', 'Cash 100']
    '''
    storageList = [[],[],[]]
    with open(fileName, 'r') as file:
        line = file.readline() # the D0-POS line
        cnt = 0
        listToAppendTo = storageList[cnt]
        while line:
            line = file.readline()
            if line == "\n":
                cnt += 1
                listToAppendTo = storageList[cnt]
                line = file.readline() # we can skip the header line
                continue
            else:
                if line == "":
                    continue
                listToAppendTo.append(line.strip("\n"))
    
    d0Data = storageList[0]
    transactions = storageList[1]
    d1Data = storageList[2]

    return d0Data, transactions, d1Data

def export_differences_to_reconOut_file(differences):
    '''
    Saves input differences to output file (recon.out) in cwd.
    
            Parameters:
                    differences (list): A list of differences, i.e. 
                        ['APPL 279', 'GOOG 19.25', 'Cash 100.10']
    '''
    with open('recon.out', 'w') as fileName:
        fileName.writelines("%s\n" % diff for diff in differences)


    