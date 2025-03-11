from __future__ import annotations
from enum import StrEnum


class WiredNetworkAuthenticationMethod(StrEnum):
	certificate = "certificate"
	usernameAndPassword = "usernameAndPassword"
	derivedCredential = "derivedCredential"
	unknownFutureValue = "unknownFutureValue"

