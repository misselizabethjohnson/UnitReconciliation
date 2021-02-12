import FileParsingFunctions
import AccountManagerFunctions

class Position: 
    ''' 
    This is a class to represent a position. 
      
    Attributes: 
        name (str): The name of the position
        shares (float): The number of shares owned.
    '''
    def __init__(self, name, shares):
        self.name = name
        self.shares = shares

    def __str__(self):
        '''String representation of position (as in input/output files).'''
        return '{self.name} '.format(self=self) + '{0:g}'.format(self.shares)

    def add_amount(self, amount):
        '''Adds shares to position.'''
        self.shares += amount

    def subtract_amount(self, amount):
        '''Subtracts shares from position.'''
        self.shares -= amount


class Account:
    ''' 
    This is a class to represent an account. 
      
    Attributes: 
        accountName (str): The 
        positions (dict): A dictionary of position objects, 
            i.e. {"APPL": Position("APPL", 3)}
        cash (float): The amount of cash in account.
    '''
    def __init__(self, accountName):
        self.accountName = accountName
        self.positions = {} # initialization
        self.cash = 0 # initialization

    def __str__(self):
        '''String representation of account cash and positions (as in input/output files).'''
        outputPositions = "".join(["%s\n" % str(pos) for pos in list(self.positions.values())])
        return "Cash {self.cash} \n%s".format(self=self) % outputPositions

    def initialize_position(self, positionName, shares):
        '''Creates a new position object and adds to self.positions.'''
        newPosition = Position(positionName, shares)
        self.positions[positionName] = newPosition
    
    def remove_position(self, positionName):
        '''Removes a position object from self.positions.'''
        del self.positions[positionName]

    def buy(self, positionName, shares, cost):
        '''Buys shares of a position.'''
        if positionName in self.positions.keys():
            self.positions[positionName].add_amount(shares)
        else:
            self.initialize_position(positionName, shares)
        self.cash -= cost

    def sell(self, positionName, shares, cost):
        '''Sells shares of a position.'''
        if positionName in self.positions.keys():
            self.positions[positionName].subtract_amount(shares)
        else:
            self.initialize_position(positionName, -shares)
        self.cash += cost

        # check if totally gone
        if self.positions[positionName].shares == 0:
            self.remove_position(positionName)
    
    def deposit_cash(self, amount):
        '''Deposits cash into account.'''
        self.cash += amount
    
    def pay_fee(self, amount):
        '''Pays amount of cash from account.'''
        self.cash -= amount

    
if __name__ == "__main__":
    # parse input file
    d0Data, transactions, d1Data = FileParsingFunctions.open_and_parse_file("recon.in")

    # create initial account
    initAccount = AccountManagerFunctions.generate_account(d0Data, "D0-POS")

    # create account to represent what was reported
    reportedAccount = AccountManagerFunctions.generate_account(d1Data, "D1-POS")

    # perform transactions to get what actual final account position should be
    accountAfterTransactions = AccountManagerFunctions.perform_transactions(transactions, initAccount)

    # calculate differences
    differences = AccountManagerFunctions.compare_account(accountAfterTransactions, reportedAccount)

    # export to output file
    FileParsingFunctions.export_differences_to_reconOut_file(differences)

    print("recon.out successfully created")