import hashlib, uuid
# only store the salt and hash on the server.

salt = uuid.uuid4().hex
hashed_password = hashlib.sha512(password + salt).hexdigest()