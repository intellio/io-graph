from __future__ import annotations
from enum import StrEnum


class AndroidDeviceOwnerDelegatedAppScopeType(StrEnum):
	unspecified = "unspecified"
	certificateInstall = "certificateInstall"
	captureNetworkActivityLog = "captureNetworkActivityLog"
	captureSecurityLog = "captureSecurityLog"
	unknownFutureValue = "unknownFutureValue"

