import UnitReconciliation

def generate_account(data, accountName):
    '''
    Returns an Account object based on input data.

            Parameters:
                    data (list): A list of positions and cash, i.e. 
                        ['APPL 20', 'Cash 100.10', 'GOOG 30.75']
                    accountName (str): A name for the Account
            Returns:
                    theAccount (UnitReconciliation.Account): Account 
    '''
    theAccount = UnitReconciliation.Account(accountName)

    for item in data:
        lineItems = item.split(" ")
        if lineItems[0] == "Cash":
            theAccount.deposit_cash(float(lineItems[1]))
        else:
            theAccount.initialize_position(lineItems[0], float(lineItems[1]))

    return theAccount
        
def perform_transactions(transactions, accountObject):
    '''
    Returns an Account object based on input transactions.

            Parameters:
                    transactions (list): A list of transactions, i.e. 
                        ['APPL BUY 1 100.10', 'GOOG SELL 11.5 22']
                    accountObject (UnitReconciliation.Account): Account
            Returns:
                    accountObject (UnitReconciliation.Account): Account 
    '''
    for trans in transactions:
        transactionEntries = trans.split(" ")
        if transactionEntries[0] == "Cash":
            if transactionEntries[1] == "DEPOSIT":
                accountObject.deposit_cash(float(transactionEntries[3]))
            elif transactionEntries[1] == "FEE":
                accountObject.pay_fee(float(transactionEntries[3]))
            else:
                raise ValueError("Cash transaction type not understood.")
        else:
            if transactionEntries[1] == "BUY":
                accountObject.buy(transactionEntries[0], float(transactionEntries[2]), 
                    float(transactionEntries[3]))
            elif transactionEntries[1] == "SELL":
                accountObject.sell(transactionEntries[0], float(transactionEntries[2]), 
                    float(transactionEntries[3]))
            elif transactionEntries[1] == "DIVIDEND":
                accountObject.deposit_cash(float(transactionEntries[3]))

    return accountObject

def compare_account(baseAccount, otherAccount):
    '''
    Returns an list of differences between two Accounts.

            Parameters:
                    baseAccount (UnitReconciliation.Account): Account (differences
                        will be with respect to this input)
                    otherAccount (UnitReconciliation.Account): Account
            Returns:
                    differences (list): A list of differences, i.e. 
                        ['APPL 279', 'GOOG 19.25', 'Cash 100.10']
    '''
    differences = [] # initialization

    # compare cash
    diffCash = otherAccount.cash - baseAccount.cash
    if diffCash != 0:
        differences.append("Cash {0:g}".format(diffCash))

    # compare positions
    for pos in list(baseAccount.positions.values()):

        if pos.name in otherAccount.positions.keys():
            # it exists in the other account, now compare values
            diff = otherAccount.positions[pos.name].shares - pos.shares
            if diff != 0:
                differences.append("%s {0:g}".format(diff) % pos.name)   
            # remove from otherAccount so we keep track of seeing it
            otherAccount.remove_position(pos.name)

        else:
            differences.append("%s {0:g}".format(-pos.shares) % pos.name)
    
    if len(otherAccount.positions) > 0:
        for remainingPos in list(otherAccount.positions.values()):
            differences.append("%s {0:g}".format(remainingPos.shares) % remainingPos.name)

    return differences

