from __future__ import annotations
from enum import StrEnum


class MessagingRedirectAppType(StrEnum):
	anyApp = "anyApp"
	anyManagedApp = "anyManagedApp"
	specificApps = "specificApps"
	blocked = "blocked"

