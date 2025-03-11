from __future__ import annotations
from enum import StrEnum


class WiFiAuthenticationMethod(StrEnum):
	certificate = "certificate"
	usernameAndPassword = "usernameAndPassword"
	derivedCredential = "derivedCredential"

