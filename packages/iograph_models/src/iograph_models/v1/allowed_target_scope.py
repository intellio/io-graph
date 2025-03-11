from __future__ import annotations
from enum import StrEnum


class AllowedTargetScope(StrEnum):
	notSpecified = "notSpecified"
	specificDirectoryUsers = "specificDirectoryUsers"
	specificConnectedOrganizationUsers = "specificConnectedOrganizationUsers"
	specificDirectoryServicePrincipals = "specificDirectoryServicePrincipals"
	allMemberUsers = "allMemberUsers"
	allDirectoryUsers = "allDirectoryUsers"
	allDirectoryServicePrincipals = "allDirectoryServicePrincipals"
	allConfiguredConnectedOrganizationUsers = "allConfiguredConnectedOrganizationUsers"
	allExternalUsers = "allExternalUsers"
	unknownFutureValue = "unknownFutureValue"

