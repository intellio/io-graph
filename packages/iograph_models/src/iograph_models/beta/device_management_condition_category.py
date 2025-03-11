from __future__ import annotations
from enum import StrEnum


class DeviceManagementConditionCategory(StrEnum):
	provisionFailures = "provisionFailures"
	imageUploadFailures = "imageUploadFailures"
	azureNetworkConnectionCheckFailures = "azureNetworkConnectionCheckFailures"
	cloudPcInGracePeriod = "cloudPcInGracePeriod"
	frontlineInsufficientLicenses = "frontlineInsufficientLicenses"
	cloudPcConnectionErrors = "cloudPcConnectionErrors"
	cloudPcHostHealthCheckFailures = "cloudPcHostHealthCheckFailures"
	cloudPcZoneOutage = "cloudPcZoneOutage"
	unknownFutureValue = "unknownFutureValue"
	frontlineBufferUsageDuration = "frontlineBufferUsageDuration"
	frontlineBufferUsageThreshold = "frontlineBufferUsageThreshold"

