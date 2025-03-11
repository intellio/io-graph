from __future__ import annotations
from enum import StrEnum


class MacOSSoftwareUpdateBehavior(StrEnum):
	notConfigured = "notConfigured"
	default = "default"
	downloadOnly = "downloadOnly"
	installASAP = "installASAP"
	notifyOnly = "notifyOnly"
	installLater = "installLater"

