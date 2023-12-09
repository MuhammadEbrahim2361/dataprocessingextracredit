class InMemoryDB:
    def __init__(self):
        self.map = {}
        self.tempMap = {}
        self.open = False

    def rollback(self):
        if not self.open:
            raise Exception("There is no open transactions")
        self.open = False
        self.tempMap = {}

    def begin_transaction(self):
        if self.open:
            raise Exception("Transaction cannot begin more than once")
        self.open = True

    def put(self, key, val):
        if not self.open:
            raise Exception("There is no transaction in progress")
        self.tempMap[key] = val

    def get(self, key):
        return self.map.get(key, None) # Returns the key's value or None

    def commit(self):
        if not self.open:
            raise Exception("There is no open transactions")
        self.open = False
        self.map.update(self.tempMap)
        self.tempMap = {}


print("Start of database:")
print("Type 'DIP' to exit the program. Type 'MANAGER' for a list of all possible commands for this database. \n")

program = True
database = InMemoryDB()

while program:
    user_input = input("Order: ")
    if user_input == "Begin Transaction":
        database.begin_transaction()
    elif user_input == "Rollback":
        database.rollback()
    elif user_input == "Put":
        key = input("Key: \n")
        value = input("Value:\n")
        database.put(key, value)
    elif user_input == "Get":
        key = input("Enter Key: \n")
        print(database.get(key))
    elif user_input == "Commit":
        database.commit()
    elif user_input == "MANAGER":
        print("All Commands:")
        print("Begin Transaction")
        print("Rollback")
        print("Put")
        print("Get")
        print("Commit")
    elif user_input == "DIP":
        program = False
    else:
        print("Invalid command. Type 'MANAGER' for a list of all possible commands for this database.\n")