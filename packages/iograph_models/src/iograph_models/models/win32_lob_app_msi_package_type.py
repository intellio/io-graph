from __future__ import annotations
from enum import Enum


class Win32LobAppMsiPackageType(Enum):
	perMachine = "perMachine"
	perUser = "perUser"
	dualPurpose = "dualPurpose"

