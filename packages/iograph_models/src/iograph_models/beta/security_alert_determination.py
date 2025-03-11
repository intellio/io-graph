from __future__ import annotations
from enum import StrEnum


class SecurityAlertDetermination(StrEnum):
	unknown = "unknown"
	apt = "apt"
	malware = "malware"
	securityPersonnel = "securityPersonnel"
	securityTesting = "securityTesting"
	unwantedSoftware = "unwantedSoftware"
	other = "other"
	multiStagedAttack = "multiStagedAttack"
	compromisedAccount = "compromisedAccount"
	phishing = "phishing"
	maliciousUserActivity = "maliciousUserActivity"
	notMalicious = "notMalicious"
	notEnoughDataToValidate = "notEnoughDataToValidate"
	confirmedActivity = "confirmedActivity"
	lineOfBusinessApplication = "lineOfBusinessApplication"
	unknownFutureValue = "unknownFutureValue"

