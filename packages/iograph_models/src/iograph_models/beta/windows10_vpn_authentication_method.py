from __future__ import annotations
from enum import StrEnum


class Windows10VpnAuthenticationMethod(StrEnum):
	certificate = "certificate"
	usernameAndPassword = "usernameAndPassword"
	customEapXml = "customEapXml"
	derivedCredential = "derivedCredential"

