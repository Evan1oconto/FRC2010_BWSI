"""a simple transaction database so that we know how to use databases"""

import json
import os
import os.path
import random
import string
from Crypto.PublicKey import RSA
from Crypto import Random

# don't forget!!!! using AES mode CTR


class DB(object):
    def __init__(self, db_path="transactions.json"):
        self.path = db_path

    def close(self):
        """close the database connection"""
        pass

    def init_db(self):
        """initialize database with file at filepath"""
        with open(self.path, 'w') as f:
            f.write(json.dumps({'Transaction ID': {}}))

    def exists(self):
        return os.path.exists(self.path)

    def modify(self, table, k, subks, vs):
        with open(self.path, 'r') as f:
            db = json.loads(f.read())

        try:
            for subk, v in zip(subks, vs):
                if k not in db[table]:
                    db[table][k] = {}
                db[table][k][subk] = v
        except KeyboardInterrupt:
            return False

        with open(self.path, 'w') as f:
            f.write(json.dumps(db))

        return True

    def read(self, table, k, subk):
        with open(self.path, 'r') as f:
            db = json.loads(f.read())

        try:
            return db[table][k][subk]
        except KeyError:
            return None

    def new_transaction(self, trans_id, trans_key):
        return self.modify("Transaction ID", trans_id, ["Transaction AES key"], [trans_key])

    def get_key(self, trans_id):
        return self.read("Transaction ID", trans_id, "Transaction AES key")


random_generator = Random.new().read

transaction_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
transaction_AES_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(128)])

transactions = DB(db_path="transactions.json")
transactions.init_db()
transactions.new_transaction(transaction_id, transaction_AES_key)

print transaction_id
print transaction_AES_key

ATM_keys = RSA.generate(2048, random_generator)
ATM_public_key = ATM_keys.publickey()

bank_package_1 = transaction_id + ", " + transaction_AES_key
bank_package_1_encrypted = ATM_public_key.encrypt(bank_package_1, ATM_public_key)

print transactions.get_key(transaction_id)
