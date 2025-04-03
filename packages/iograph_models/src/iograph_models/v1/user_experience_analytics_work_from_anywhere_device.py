from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class UserExperienceAnalyticsWorkFromAnywhereDevice(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice"] = Field(alias="@odata.type", default="#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice")
	autoPilotProfileAssigned: Optional[bool] = Field(alias="autoPilotProfileAssigned", default=None,)
	autoPilotRegistered: Optional[bool] = Field(alias="autoPilotRegistered", default=None,)
	azureAdDeviceId: Optional[str] = Field(alias="azureAdDeviceId", default=None,)
	azureAdJoinType: Optional[str] = Field(alias="azureAdJoinType", default=None,)
	azureAdRegistered: Optional[bool] = Field(alias="azureAdRegistered", default=None,)
	cloudIdentityScore: float | str | ReferenceNumeric
	cloudManagementScore: float | str | ReferenceNumeric
	cloudProvisioningScore: float | str | ReferenceNumeric
	compliancePolicySetToIntune: Optional[bool] = Field(alias="compliancePolicySetToIntune", default=None,)
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)
	deviceName: Optional[str] = Field(alias="deviceName", default=None,)
	healthStatus: Optional[UserExperienceAnalyticsHealthState | str] = Field(alias="healthStatus", default=None,)
	isCloudManagedGatewayEnabled: Optional[bool] = Field(alias="isCloudManagedGatewayEnabled", default=None,)
	managedBy: Optional[str] = Field(alias="managedBy", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	osCheckFailed: Optional[bool] = Field(alias="osCheckFailed", default=None,)
	osDescription: Optional[str] = Field(alias="osDescription", default=None,)
	osVersion: Optional[str] = Field(alias="osVersion", default=None,)
	otherWorkloadsSetToIntune: Optional[bool] = Field(alias="otherWorkloadsSetToIntune", default=None,)
	ownership: Optional[str] = Field(alias="ownership", default=None,)
	processor64BitCheckFailed: Optional[bool] = Field(alias="processor64BitCheckFailed", default=None,)
	processorCoreCountCheckFailed: Optional[bool] = Field(alias="processorCoreCountCheckFailed", default=None,)
	processorFamilyCheckFailed: Optional[bool] = Field(alias="processorFamilyCheckFailed", default=None,)
	processorSpeedCheckFailed: Optional[bool] = Field(alias="processorSpeedCheckFailed", default=None,)
	ramCheckFailed: Optional[bool] = Field(alias="ramCheckFailed", default=None,)
	secureBootCheckFailed: Optional[bool] = Field(alias="secureBootCheckFailed", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	storageCheckFailed: Optional[bool] = Field(alias="storageCheckFailed", default=None,)
	tenantAttached: Optional[bool] = Field(alias="tenantAttached", default=None,)
	tpmCheckFailed: Optional[bool] = Field(alias="tpmCheckFailed", default=None,)
	upgradeEligibility: Optional[OperatingSystemUpgradeEligibility | str] = Field(alias="upgradeEligibility", default=None,)
	windowsScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .operating_system_upgrade_eligibility import OperatingSystemUpgradeEligibility
