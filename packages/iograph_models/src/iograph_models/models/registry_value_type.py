from __future__ import annotations
from enum import Enum


class RegistryValueType(Enum):
	unknown = "unknown"
	binary = "binary"
	dword = "dword"
	dwordLittleEndian = "dwordLittleEndian"
	dwordBigEndian = "dwordBigEndian"
	expandSz = "expandSz"
	link = "link"
	multiSz = "multiSz"
	none = "none"
	qword = "qword"
	qwordlittleEndian = "qwordlittleEndian"
	sz = "sz"
	unknownFutureValue = "unknownFutureValue"

