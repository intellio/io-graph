from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsMinimumSessionSecurity(StrEnum):
	none = "none"
	requireNtmlV2SessionSecurity = "requireNtmlV2SessionSecurity"
	require128BitEncryption = "require128BitEncryption"
	ntlmV2And128BitEncryption = "ntlmV2And128BitEncryption"

