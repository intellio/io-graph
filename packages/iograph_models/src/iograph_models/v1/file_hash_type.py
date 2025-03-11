from __future__ import annotations
from enum import StrEnum


class FileHashType(StrEnum):
	unknown = "unknown"
	sha1 = "sha1"
	sha256 = "sha256"
	md5 = "md5"
	authenticodeHash256 = "authenticodeHash256"
	lsHash = "lsHash"
	ctph = "ctph"
	unknownFutureValue = "unknownFutureValue"

