from __future__ import annotations
from enum import StrEnum


class ManagedAppRemediationAction(StrEnum):
	block = "block"
	wipe = "wipe"
	warn = "warn"
	blockWhenSettingIsSupported = "blockWhenSettingIsSupported"

