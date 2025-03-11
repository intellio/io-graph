from __future__ import annotations
from enum import StrEnum


class CloudPcRemoteActionName(StrEnum):
	unknown = "unknown"
	restart = "restart"
	rename = "rename"
	resize = "resize"
	restore = "restore"
	reprovision = "reprovision"
	changeUserAccountType = "changeUserAccountType"
	troubleshoot = "troubleshoot"
	placeUnderReview = "placeUnderReview"
	unknownFutureValue = "unknownFutureValue"
	createSnapshot = "createSnapshot"
	powerOn = "powerOn"
	powerOff = "powerOff"
	moveRegion = "moveRegion"

