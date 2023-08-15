import hmac
import hashlib

def validate_hash(entered, stored):
    stored = bytes.fromhex(stored)

    list1 = []
    start_b = 0
    list1.append(stored[start_b : start_b + 16])
    ext_salt = list1[0]

    list1.clear()

    start_b = 16
    list1.append(stored[start_b : start_b + 64])
    ext_hash = list1[0]

    entered_byte = bytes(entered, "utf-8")

    return hmac.compare_digest(
        ext_hash,
        hashlib.pbkdf2_hmac('sha512', entered_byte, ext_salt, 100000)
    )
