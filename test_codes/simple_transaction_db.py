"""a simple transaction database so that we know how to use databases"""

import json
import os
import os.path

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
