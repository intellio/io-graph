from __future__ import annotations
from enum import StrEnum


class DiffieHellmanGroup(StrEnum):
	group1 = "group1"
	group2 = "group2"
	group14 = "group14"
	ecp256 = "ecp256"
	ecp384 = "ecp384"
	group24 = "group24"

