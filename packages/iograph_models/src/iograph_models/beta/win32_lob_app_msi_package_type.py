from __future__ import annotations
from enum import StrEnum


class Win32LobAppMsiPackageType(StrEnum):
	perMachine = "perMachine"
	perUser = "perUser"
	dualPurpose = "dualPurpose"

