from __future__ import annotations
from enum import StrEnum


class AutomaticUpdateMode(StrEnum):
	userDefined = "userDefined"
	notifyDownload = "notifyDownload"
	autoInstallAtMaintenanceTime = "autoInstallAtMaintenanceTime"
	autoInstallAndRebootAtMaintenanceTime = "autoInstallAndRebootAtMaintenanceTime"
	autoInstallAndRebootAtScheduledTime = "autoInstallAndRebootAtScheduledTime"
	autoInstallAndRebootWithoutEndUserControl = "autoInstallAndRebootWithoutEndUserControl"

