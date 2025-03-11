from __future__ import annotations
from enum import StrEnum


class SingleSignOnMode(StrEnum):
	none = "none"
	onPremisesKerberos = "onPremisesKerberos"
	saml = "saml"
	pingHeaderBased = "pingHeaderBased"
	aadHeaderBased = "aadHeaderBased"
	oAuthToken = "oAuthToken"
	unknownFutureValue = "unknownFutureValue"

