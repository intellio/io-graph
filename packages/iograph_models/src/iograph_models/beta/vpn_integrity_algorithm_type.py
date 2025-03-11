from __future__ import annotations
from enum import StrEnum


class VpnIntegrityAlgorithmType(StrEnum):
	sha2_256 = "sha2_256"
	sha1_96 = "sha1_96"
	sha1_160 = "sha1_160"
	sha2_384 = "sha2_384"
	sha2_512 = "sha2_512"
	md5 = "md5"

