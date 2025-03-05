from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class UserExperienceAnalyticsWorkFromAnywhereDevice(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	autoPilotProfileAssigned: Optional[bool] = Field(default=None,alias="autoPilotProfileAssigned",)
	autoPilotRegistered: Optional[bool] = Field(default=None,alias="autoPilotRegistered",)
	azureAdDeviceId: Optional[str] = Field(default=None,alias="azureAdDeviceId",)
	azureAdJoinType: Optional[str] = Field(default=None,alias="azureAdJoinType",)
	azureAdRegistered: Optional[bool] = Field(default=None,alias="azureAdRegistered",)
	cloudIdentityScore: float | str | ReferenceNumeric
	cloudManagementScore: float | str | ReferenceNumeric
	cloudProvisioningScore: float | str | ReferenceNumeric
	compliancePolicySetToIntune: Optional[bool] = Field(default=None,alias="compliancePolicySetToIntune",)
	deviceId: Optional[str] = Field(default=None,alias="deviceId",)
	deviceName: Optional[str] = Field(default=None,alias="deviceName",)
	healthStatus: Optional[UserExperienceAnalyticsHealthState] = Field(default=None,alias="healthStatus",)
	isCloudManagedGatewayEnabled: Optional[bool] = Field(default=None,alias="isCloudManagedGatewayEnabled",)
	managedBy: Optional[str] = Field(default=None,alias="managedBy",)
	manufacturer: Optional[str] = Field(default=None,alias="manufacturer",)
	model: Optional[str] = Field(default=None,alias="model",)
	osCheckFailed: Optional[bool] = Field(default=None,alias="osCheckFailed",)
	osDescription: Optional[str] = Field(default=None,alias="osDescription",)
	osVersion: Optional[str] = Field(default=None,alias="osVersion",)
	otherWorkloadsSetToIntune: Optional[bool] = Field(default=None,alias="otherWorkloadsSetToIntune",)
	ownership: Optional[str] = Field(default=None,alias="ownership",)
	processor64BitCheckFailed: Optional[bool] = Field(default=None,alias="processor64BitCheckFailed",)
	processorCoreCountCheckFailed: Optional[bool] = Field(default=None,alias="processorCoreCountCheckFailed",)
	processorFamilyCheckFailed: Optional[bool] = Field(default=None,alias="processorFamilyCheckFailed",)
	processorSpeedCheckFailed: Optional[bool] = Field(default=None,alias="processorSpeedCheckFailed",)
	ramCheckFailed: Optional[bool] = Field(default=None,alias="ramCheckFailed",)
	secureBootCheckFailed: Optional[bool] = Field(default=None,alias="secureBootCheckFailed",)
	serialNumber: Optional[str] = Field(default=None,alias="serialNumber",)
	storageCheckFailed: Optional[bool] = Field(default=None,alias="storageCheckFailed",)
	tenantAttached: Optional[bool] = Field(default=None,alias="tenantAttached",)
	tpmCheckFailed: Optional[bool] = Field(default=None,alias="tpmCheckFailed",)
	upgradeEligibility: Optional[OperatingSystemUpgradeEligibility] = Field(default=None,alias="upgradeEligibility",)
	windowsScore: float | str | ReferenceNumeric
	workFromAnywhereScore: float | str | ReferenceNumeric

from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric
from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
from .operating_system_upgrade_eligibility import OperatingSystemUpgradeEligibility
from .reference_numeric import ReferenceNumeric
from .reference_numeric import ReferenceNumeric

