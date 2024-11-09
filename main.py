#!/usr/bin/env python3
import sys

class UnrecognizedCommandException(Exception):
    pass

class UnrecognizedStatementException(Exception):
    pass

class Statement:

    def __init__(self, query):
        self.query = query

    def execute(self):
        raise NotImplementedError("Must use a child class of statement")

class SelectStatement(Statement):

    def execute(self):
        print("Executing select statement")

class InsertStatement(Statement):
    
    def execute(self):
        print("Executing insert statement")



def print_prompt():
    print("db > ", end='', flush=True)

def execute_meta_command(command):
    if command == ".exit": 
        sys.exit(0)
    else:
        raise UnrecognizedCommandException(f"Unrecognized command '{command}'.")

def prepare_statement(query):  
    if query.startswith("select"):
        return SelectStatement(query)
    elif query.startswith("insert"):
        return InsertStatement(query)
    else: 
        raise UnrecognizedStatementException(f"Unrecognized statement '{query}'.")


def main():
    while True:
        print_prompt()
        user_input = input().strip()

        # Meta command
        if user_input[0] == ".":
            try:
                execute_meta_command(user_input)
            except UnrecognizedCommandException as e:
                print(e)
        else:
            try:
                statement = prepare_statement(user_input)
            except UnrecognizedStatementException as e:
                print(e)
                continue
            statement.execute()


if __name__ == "__main__":
    main()