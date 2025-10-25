from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def compare_hash(plain_text, hashed_text):
    return bcrypt_context.verify(plain_text, hashed_text)

def get_hash(plain_text):
    return bcrypt_context.hash(plain_text)