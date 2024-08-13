import bcrypt

# Hash a password using bcrypt


def hash_password(password: str):
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password
