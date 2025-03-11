from __future__ import annotations
from enum import StrEnum


class MacOSSoftwareUpdateState(StrEnum):
	success = "success"
	downloading = "downloading"
	downloaded = "downloaded"
	installing = "installing"
	idle = "idle"
	available = "available"
	scheduled = "scheduled"
	downloadFailed = "downloadFailed"
	downloadInsufficientSpace = "downloadInsufficientSpace"
	downloadInsufficientPower = "downloadInsufficientPower"
	downloadInsufficientNetwork = "downloadInsufficientNetwork"
	installInsufficientSpace = "installInsufficientSpace"
	installInsufficientPower = "installInsufficientPower"
	installFailed = "installFailed"
	commandFailed = "commandFailed"

