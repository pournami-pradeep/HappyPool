import bcrypt


def hash_function(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'),salt)
    return hashed
