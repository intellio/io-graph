from __future__ import annotations
from enum import StrEnum


class RestrictionTrigger(StrEnum):
	copyPaste = "copyPaste"
	copyToNetworkShare = "copyToNetworkShare"
	copyToRemovableMedia = "copyToRemovableMedia"
	screenCapture = "screenCapture"
	print = "print"
	cloudEgress = "cloudEgress"
	unallowedApps = "unallowedApps"

