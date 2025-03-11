from __future__ import annotations
from enum import StrEnum


class RequiredLicenses(StrEnum):
	notApplicable = "notApplicable"
	microsoftEntraIdFree = "microsoftEntraIdFree"
	microsoftEntraIdP1 = "microsoftEntraIdP1"
	microsoftEntraIdP2 = "microsoftEntraIdP2"
	microsoftEntraIdGovernance = "microsoftEntraIdGovernance"
	microsoftEntraWorkloadId = "microsoftEntraWorkloadId"
	unknownFutureValue = "unknownFutureValue"

