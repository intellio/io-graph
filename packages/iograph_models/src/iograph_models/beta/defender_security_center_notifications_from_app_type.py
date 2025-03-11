from __future__ import annotations
from enum import StrEnum


class DefenderSecurityCenterNotificationsFromAppType(StrEnum):
	notConfigured = "notConfigured"
	blockNoncriticalNotifications = "blockNoncriticalNotifications"
	blockAllNotifications = "blockAllNotifications"

