from __future__ import annotations
from enum import StrEnum


class KerberosSignOnMappingAttributeType(StrEnum):
	userPrincipalName = "userPrincipalName"
	onPremisesUserPrincipalName = "onPremisesUserPrincipalName"
	userPrincipalUsername = "userPrincipalUsername"
	onPremisesUserPrincipalUsername = "onPremisesUserPrincipalUsername"
	onPremisesSAMAccountName = "onPremisesSAMAccountName"

