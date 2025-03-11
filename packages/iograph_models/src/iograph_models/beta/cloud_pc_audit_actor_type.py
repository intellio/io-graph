from __future__ import annotations
from enum import StrEnum


class CloudPcAuditActorType(StrEnum):
	itPro = "itPro"
	application = "application"
	partner = "partner"
	unknownFutureValue = "unknownFutureValue"

