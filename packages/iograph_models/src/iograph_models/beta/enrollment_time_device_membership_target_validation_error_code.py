from __future__ import annotations
from enum import StrEnum


class EnrollmentTimeDeviceMembershipTargetValidationErrorCode(StrEnum):
	unknown = "unknown"
	securityGroupNotFound = "securityGroupNotFound"
	notSecurityGroup = "notSecurityGroup"
	notStaticSecurityGroup = "notStaticSecurityGroup"
	firstPartyAppNotAnOwner = "firstPartyAppNotAnOwner"
	securityGroupNotInCallerScope = "securityGroupNotInCallerScope"
	unknownFutureValue = "unknownFutureValue"

