from __future__ import annotations
from enum import StrEnum


class ClientCredentialType(StrEnum):
	none = "none"
	clientSecret = "clientSecret"
	clientAssertion = "clientAssertion"
	federatedIdentityCredential = "federatedIdentityCredential"
	managedIdentity = "managedIdentity"
	certificate = "certificate"
	unknownFutureValue = "unknownFutureValue"

