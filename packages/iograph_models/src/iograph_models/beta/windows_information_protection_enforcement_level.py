from __future__ import annotations
from enum import StrEnum


class WindowsInformationProtectionEnforcementLevel(StrEnum):
	noProtection = "noProtection"
	encryptAndAuditOnly = "encryptAndAuditOnly"
	encryptAuditAndPrompt = "encryptAuditAndPrompt"
	encryptAuditAndBlock = "encryptAuditAndBlock"

