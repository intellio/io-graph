from __future__ import annotations
from enum import Enum


class AllowedTargetScope(Enum):
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

