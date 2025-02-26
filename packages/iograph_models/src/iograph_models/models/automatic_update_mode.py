from __future__ import annotations
from enum import Enum


class AutomaticUpdateMode(Enum):
	userDefined = "userDefined"
	notifyDownload = "notifyDownload"
	autoInstallAtMaintenanceTime = "autoInstallAtMaintenanceTime"
	autoInstallAndRebootAtMaintenanceTime = "autoInstallAndRebootAtMaintenanceTime"
	autoInstallAndRebootAtScheduledTime = "autoInstallAndRebootAtScheduledTime"
	autoInstallAndRebootWithoutEndUserControl = "autoInstallAndRebootWithoutEndUserControl"

