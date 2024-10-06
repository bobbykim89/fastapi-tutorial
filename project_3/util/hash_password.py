import bcrypt

# Hash a password using bcrypt


def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    string_password = hashed_password.decode('utf-8')
    return string_password
