import os
import hashlib
from ed25519 import SigningKey
import bech32

def generate_sui_wallet():
    private_key = os.urandom(32)
    signing_key = SigningKey(private_key)
    public_key = signing_key.verifying_key.to_bytes()

    # Sui address: 0x00 flag + 32-byte pubkey → sha3-256 → bech32 "sui"
    payload = b'\x00' + public_key
    hashed = hashlib.sha3_256(payload).digest()
    addr = bech32.bech32_encode("sui", bech32.convertbits(hashed, 8, 5, True))

    return {
        "address": addr,
        "private_key_hex": private_key.hex(),
        "public_key_hex": public_key.hex()
    }

print("SUI Wallet Generator\n")
print("-" * 70)

for i in range(10):
    wallet = generate_sui_wallet()
    print(f"Кошелёк {i+1}")
    print(f"Адрес:         {wallet['address']}")
    print(f"Приватный ключ: {wallet['private_key_hex']}")
    print(f"Публичный ключ: {wallet['public_key_hex']}")
    print("-" * 70)
