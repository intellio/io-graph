from __future__ import annotations
from enum import StrEnum


class LocalSecurityOptionsSmartCardRemovalBehaviorType(StrEnum):
	noAction = "noAction"
	lockWorkstation = "lockWorkstation"
	forceLogoff = "forceLogoff"
	disconnectRemoteDesktopSession = "disconnectRemoteDesktopSession"

