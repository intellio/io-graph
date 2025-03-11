from __future__ import annotations
from enum import StrEnum


class EasAuthenticationMethod(StrEnum):
	usernameAndPassword = "usernameAndPassword"
	certificate = "certificate"
	derivedCredential = "derivedCredential"

