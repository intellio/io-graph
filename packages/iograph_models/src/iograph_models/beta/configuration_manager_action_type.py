from __future__ import annotations
from enum import StrEnum


class ConfigurationManagerActionType(StrEnum):
	refreshMachinePolicy = "refreshMachinePolicy"
	refreshUserPolicy = "refreshUserPolicy"
	wakeUpClient = "wakeUpClient"
	appEvaluation = "appEvaluation"
	quickScan = "quickScan"
	fullScan = "fullScan"
	windowsDefenderUpdateSignatures = "windowsDefenderUpdateSignatures"

