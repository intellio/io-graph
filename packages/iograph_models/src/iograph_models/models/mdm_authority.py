from __future__ import annotations
from enum import Enum


class MdmAuthority(Enum):
	unknown = "unknown"
	intune = "intune"
	sccm = "sccm"
	office365 = "office365"

