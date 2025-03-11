from __future__ import annotations
from enum import StrEnum


class SubjectAlternativeNameType(StrEnum):
	none = "none"
	emailAddress = "emailAddress"
	userPrincipalName = "userPrincipalName"
	customAzureADAttribute = "customAzureADAttribute"
	domainNameService = "domainNameService"
	universalResourceIdentifier = "universalResourceIdentifier"

