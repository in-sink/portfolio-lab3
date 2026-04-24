#!/usr/bin/env python3
import hashlib
import sys

if len(sys.argv) != 2:
    print("Usage: python change_password.py <new_password>")
    sys.exit(1)

new_password = sys.argv[1]
hash_obj = hashlib.sha256(new_password.encode())
new_hash = hash_obj.hexdigest()

# Read protected.html
with open('protected.html', 'r') as f:
    content = f.read()

# Replace the hash
old_hash = '96db3ecc8355c49b5736ca38b06e6dbb151eb6aac88cc531e074b6c91871aab9'  # default
new_content = content.replace(old_hash, new_hash)

# Write back
with open('protected.html', 'w') as f:
    f.write(new_content)

print(f"Password changed. New hash: {new_hash}")