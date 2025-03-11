from __future__ import annotations
from enum import StrEnum


class ZebraFotaErrorCode(StrEnum):
	success = "success"
	noDevicesFoundInSelectedAadGroups = "noDevicesFoundInSelectedAadGroups"
	noIntuneDevicesFoundInSelectedAadGroups = "noIntuneDevicesFoundInSelectedAadGroups"
	noZebraFotaEnrolledDevicesFoundForCurrentTenant = "noZebraFotaEnrolledDevicesFoundForCurrentTenant"
	noZebraFotaEnrolledDevicesFoundInSelectedAadGroups = "noZebraFotaEnrolledDevicesFoundInSelectedAadGroups"
	noZebraFotaDevicesFoundForSelectedDeviceModel = "noZebraFotaDevicesFoundForSelectedDeviceModel"
	zebraFotaCreateDeploymentRequestFailure = "zebraFotaCreateDeploymentRequestFailure"
	unknownFutureValue = "unknownFutureValue"

