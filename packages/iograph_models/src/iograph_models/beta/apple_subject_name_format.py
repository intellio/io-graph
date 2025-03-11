from __future__ import annotations
from enum import StrEnum


class AppleSubjectNameFormat(StrEnum):
	commonName = "commonName"
	commonNameAsEmail = "commonNameAsEmail"
	custom = "custom"
	commonNameIncludingEmail = "commonNameIncludingEmail"
	commonNameAsIMEI = "commonNameAsIMEI"
	commonNameAsSerialNumber = "commonNameAsSerialNumber"

