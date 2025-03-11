from __future__ import annotations
from enum import StrEnum


class VpnEncryptionAlgorithmType(StrEnum):
	aes256 = "aes256"
	des = "des"
	tripleDes = "tripleDes"
	aes128 = "aes128"
	aes128Gcm = "aes128Gcm"
	aes256Gcm = "aes256Gcm"
	aes192 = "aes192"
	aes192Gcm = "aes192Gcm"
	chaCha20Poly1305 = "chaCha20Poly1305"

