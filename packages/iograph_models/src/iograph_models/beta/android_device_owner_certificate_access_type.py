from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerCertificateAccessType(StrEnum):
	userApproval = "userApproval"
	specificApps = "specificApps"
	unknownFutureValue = "unknownFutureValue"

