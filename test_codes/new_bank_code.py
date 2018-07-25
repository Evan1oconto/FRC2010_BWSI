import random
import string
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
from databases import DB
import struct

# don't forget!!!! using AES mode CTR

random_generator = Random.new().read

# generates information for this transaction
transaction_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
transaction_AES_key = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(128)])

# initializes the transaction database and adds the transaction information
transactions = DB(db_path="transactions.json")
transactions.init_transaction_db()
transactions.new_transaction(transaction_id, transaction_AES_key)

# initializes the accounts database and adds some fake info
accounts = DB(db_path="accounts.json")
accounts.init_account_db()
accounts.admin_create_account("1234567891011121", "625")
accounts.set_balance("1234567891011121", "1025")
print accounts.get_balance("1234567891011121")

# prints transaction info
print transaction_id
print transaction_AES_key

# generates ATM RSA information
ATM_keys = RSA.generate(2048, random_generator)
ATM_public_key = ATM_keys.publickey()

# packages information for ATM and creates encrypted copy and hashed copy
bank_package_1 = struct.pack(">32s128s", transaction_id, transaction_AES_key)
bank_package_1_encrypted = ATM_public_key.encrypt(bank_package_1, ATM_public_key)
bank_package_1_hashed = SHA256.new(bank_package_1).hexdigest()

# prints transaction id and both the encrypted and the hashed packages
print transactions.get_key(transaction_id)
print bank_package_1_encrypted
print bank_package_1_hashed

# decrypts the encrypted package and unpacks it
decrypted = ATM_keys.decrypt(bank_package_1_encrypted)
unpacked = struct.unpack(">32s128s", decrypted)
print unpacked
