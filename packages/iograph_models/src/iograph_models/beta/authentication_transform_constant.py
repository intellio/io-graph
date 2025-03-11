from __future__ import annotations
from enum import StrEnum


class AuthenticationTransformConstant(StrEnum):
	md5_96 = "md5_96"
	sha1_96 = "sha1_96"
	sha_256_128 = "sha_256_128"
	aes128Gcm = "aes128Gcm"
	aes192Gcm = "aes192Gcm"
	aes256Gcm = "aes256Gcm"

