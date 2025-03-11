from __future__ import annotations
from enum import StrEnum


class MdmAuthority(StrEnum):
	unknown = "unknown"
	intune = "intune"
	sccm = "sccm"
	office365 = "office365"

