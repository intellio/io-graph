from __future__ import annotations
from enum import StrEnum


class NetworkaccessPfsGroup(StrEnum):
	none = "none"
	pfs1 = "pfs1"
	pfs2 = "pfs2"
	pfs14 = "pfs14"
	pfs24 = "pfs24"
	pfs2048 = "pfs2048"
	pfsmm = "pfsmm"
	ecp256 = "ecp256"
	ecp384 = "ecp384"
	unknownFutureValue = "unknownFutureValue"

