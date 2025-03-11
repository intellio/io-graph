from __future__ import annotations
from enum import StrEnum


class ManagedDeviceRemoteAction(StrEnum):
	retire = "retire"
	delete = "delete"
	fullScan = "fullScan"
	quickScan = "quickScan"
	signatureUpdate = "signatureUpdate"
	wipe = "wipe"
	customTextNotification = "customTextNotification"
	rebootNow = "rebootNow"
	setDeviceName = "setDeviceName"
	syncDevice = "syncDevice"
	deprovision = "deprovision"
	disable = "disable"
	reenable = "reenable"
	moveDeviceToOrganizationalUnit = "moveDeviceToOrganizationalUnit"
	activateDeviceEsim = "activateDeviceEsim"
	collectDiagnostics = "collectDiagnostics"
	initiateMobileDeviceManagementKeyRecovery = "initiateMobileDeviceManagementKeyRecovery"
	initiateOnDemandProactiveRemediation = "initiateOnDemandProactiveRemediation"
	unknownFutureValue = "unknownFutureValue"
	initiateDeviceAttestation = "initiateDeviceAttestation"

