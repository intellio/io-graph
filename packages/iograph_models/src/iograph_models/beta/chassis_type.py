from __future__ import annotations
from enum import StrEnum


class ChassisType(StrEnum):
	unknown = "unknown"
	desktop = "desktop"
	laptop = "laptop"
	worksWorkstation = "worksWorkstation"
	enterpriseServer = "enterpriseServer"
	phone = "phone"
	tablet = "tablet"
	mobileOther = "mobileOther"
	mobileUnknown = "mobileUnknown"

