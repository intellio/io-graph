from __future__ import annotations
from enum import StrEnum


class PerfectForwardSecrecyGroup(StrEnum):
	pfs1 = "pfs1"
	pfs2 = "pfs2"
	pfs2048 = "pfs2048"
	ecp256 = "ecp256"
	ecp384 = "ecp384"
	pfsMM = "pfsMM"
	pfs24 = "pfs24"

