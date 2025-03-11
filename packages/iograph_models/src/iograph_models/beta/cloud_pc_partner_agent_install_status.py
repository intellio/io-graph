from __future__ import annotations
from enum import StrEnum


class CloudPcPartnerAgentInstallStatus(StrEnum):
	installed = "installed"
	installFailed = "installFailed"
	installing = "installing"
	uninstalling = "uninstalling"
	uninstallFailed = "uninstallFailed"
	licensed = "licensed"
	unknownFutureValue = "unknownFutureValue"

