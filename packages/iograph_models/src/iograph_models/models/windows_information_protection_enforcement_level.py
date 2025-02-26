from __future__ import annotations
from enum import Enum


class WindowsInformationProtectionEnforcementLevel(Enum):
	noProtection = "noProtection"
	encryptAndAuditOnly = "encryptAndAuditOnly"
	encryptAuditAndPrompt = "encryptAuditAndPrompt"
	encryptAuditAndBlock = "encryptAuditAndBlock"

