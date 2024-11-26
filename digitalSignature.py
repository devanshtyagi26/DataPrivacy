from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

# Generate a private/public key pair
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    
    # Public key corresponding to the private key
    public_key = private_key.public_key()
    
    # Serialize the private key (for storage or usage)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # Serialize the public key (for sharing or verification)
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem, private_key, public_key

# Sign the document with the private key
def sign_document(document, private_key):
    signature = private_key.sign(
        document.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    
    # Return the signature in base64 encoding for easy transmission
    return base64.b64encode(signature).decode()

# Verify the signature with the public key
def verify_signature(document, signature, public_key):
    try:
        public_key.verify(
            base64.b64decode(signature),
            document.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Signature is valid!")
    except Exception as e:
        print("Signature verification failed:", e)

# Main program demonstrating the signing and verification process
def main():
    # Step 1: Generate a private/public key pair
    private_pem, public_pem, private_key, public_key = generate_keys()
    
    # Save the keys to files (optional, for reference)
    with open('private_key.pem', 'wb') as f:
        f.write(private_pem)
    with open('public_key.pem', 'wb') as f:
        f.write(public_pem)
    
    # Step 2: Create a document to sign
    document = "This is a confidential document that needs to be signed."
    print("Document to sign:", document)
    
    # Step 3: Sign the document with the private key
    signature = sign_document(document, private_key)
    print("Generated signature:", signature)
    
    # Step 4: Verify the signature using the public key
    verify_signature(document, signature, public_key)


main()