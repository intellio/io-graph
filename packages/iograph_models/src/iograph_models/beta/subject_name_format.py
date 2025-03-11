from __future__ import annotations
from enum import StrEnum


class SubjectNameFormat(StrEnum):
	commonName = "commonName"
	commonNameIncludingEmail = "commonNameIncludingEmail"
	commonNameAsEmail = "commonNameAsEmail"
	custom = "custom"
	commonNameAsIMEI = "commonNameAsIMEI"
	commonNameAsSerialNumber = "commonNameAsSerialNumber"
	commonNameAsAadDeviceId = "commonNameAsAadDeviceId"
	commonNameAsIntuneDeviceId = "commonNameAsIntuneDeviceId"
	commonNameAsDurableDeviceId = "commonNameAsDurableDeviceId"

