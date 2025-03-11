from __future__ import annotations
from enum import StrEnum


class UserPfxPaddingScheme(StrEnum):
	none = "none"
	pkcs1 = "pkcs1"
	oaepSha1 = "oaepSha1"
	oaepSha256 = "oaepSha256"
	oaepSha384 = "oaepSha384"
	oaepSha512 = "oaepSha512"

