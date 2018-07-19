import random
import string 

#Recieving the ATM's Public Key and the ATM's request for the AES key
ATM_Public_Key_e = 
ATM_Public_Key_N = 
AES_Request = 

#Generates a transaction id with random letters and numbers (ex. VhGBjfl0cYmjDxxc5N0ky8P06LvwDexE), can change length by changing green number
Transaction_id = .join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

#Receive transaction id (plaintext) 
Transaction_id_Plainstext = 

#Receive  CCN, balance value, tamper code, PIN, ATM ID (Encrypted by AES)
CCN_Encrypted_AES = 
Balance_Value_Encrypted_AES = 
Tamper_Code_Encrypted_AES = 
Pin_Encrypted_AES =
ATM_id_Encrypted AES =

#Receive  CCN, balance value, tamper code, PIN, ATM ID (Hashed)
CCN_Hashed1 = 
Balance_Hashed1 =
Tamper_Code_Hashed1 =
Pin_Hashed1 =
ATM_id_Hashed1 =
