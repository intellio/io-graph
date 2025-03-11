from __future__ import annotations
from enum import StrEnum


class VpnAuthenticationMethod(StrEnum):
	certificate = "certificate"
	usernameAndPassword = "usernameAndPassword"
	sharedSecret = "sharedSecret"
	derivedCredential = "derivedCredential"
	azureAD = "azureAD"

