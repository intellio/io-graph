from __future__ import annotations
from enum import StrEnum


class DeviceManagementAlertRuleTemplate(StrEnum):
	cloudPcProvisionScenario = "cloudPcProvisionScenario"
	cloudPcImageUploadScenario = "cloudPcImageUploadScenario"
	cloudPcOnPremiseNetworkConnectionCheckScenario = "cloudPcOnPremiseNetworkConnectionCheckScenario"
	unknownFutureValue = "unknownFutureValue"
	cloudPcInGracePeriodScenario = "cloudPcInGracePeriodScenario"
	cloudPcFrontlineInsufficientLicensesScenario = "cloudPcFrontlineInsufficientLicensesScenario"
	cloudPcInaccessibleScenario = "cloudPcInaccessibleScenario"
	cloudPcFrontlineConcurrencyScenario = "cloudPcFrontlineConcurrencyScenario"

