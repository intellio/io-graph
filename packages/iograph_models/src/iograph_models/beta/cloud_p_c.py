from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPC(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	aadDeviceId: Optional[str] = Field(alias="aadDeviceId", default=None,)
	allotmentDisplayName: Optional[str] = Field(alias="allotmentDisplayName", default=None,)
	connectionSetting: Optional[CloudPcConnectionSetting] = Field(alias="connectionSetting", default=None,)
	connectionSettings: Optional[CloudPcConnectionSettings] = Field(alias="connectionSettings", default=None,)
	connectivityResult: Optional[CloudPcConnectivityResult] = Field(alias="connectivityResult", default=None,)
	deviceRegionName: Optional[str] = Field(alias="deviceRegionName", default=None,)
	disasterRecoveryCapability: Optional[CloudPcDisasterRecoveryCapability] = Field(alias="disasterRecoveryCapability", default=None,)
	diskEncryptionState: Optional[CloudPcDiskEncryptionState | str] = Field(alias="diskEncryptionState", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	frontlineCloudPcAvailability: Optional[FrontlineCloudPcAvailability | str] = Field(alias="frontlineCloudPcAvailability", default=None,)
	gracePeriodEndDateTime: Optional[datetime] = Field(alias="gracePeriodEndDateTime", default=None,)
	imageDisplayName: Optional[str] = Field(alias="imageDisplayName", default=None,)
	lastLoginResult: Optional[CloudPcLoginResult] = Field(alias="lastLoginResult", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	lastRemoteActionResult: Optional[CloudPcRemoteActionResult] = Field(alias="lastRemoteActionResult", default=None,)
	managedDeviceId: Optional[str] = Field(alias="managedDeviceId", default=None,)
	managedDeviceName: Optional[str] = Field(alias="managedDeviceName", default=None,)
	onPremisesConnectionName: Optional[str] = Field(alias="onPremisesConnectionName", default=None,)
	osVersion: Optional[CloudPcOperatingSystem | str] = Field(alias="osVersion", default=None,)
	partnerAgentInstallResults: Optional[list[CloudPcPartnerAgentInstallResult]] = Field(alias="partnerAgentInstallResults", default=None,)
	powerState: Optional[CloudPcPowerState | str] = Field(alias="powerState", default=None,)
	productType: Optional[CloudPcProductType | str] = Field(alias="productType", default=None,)
	provisioningPolicyId: Optional[str] = Field(alias="provisioningPolicyId", default=None,)
	provisioningPolicyName: Optional[str] = Field(alias="provisioningPolicyName", default=None,)
	provisioningType: Optional[CloudPcProvisioningType | str] = Field(alias="provisioningType", default=None,)
	scopeIds: Optional[list[str]] = Field(alias="scopeIds", default=None,)
	servicePlanId: Optional[str] = Field(alias="servicePlanId", default=None,)
	servicePlanName: Optional[str] = Field(alias="servicePlanName", default=None,)
	servicePlanType: Optional[CloudPcServicePlanType | str] = Field(alias="servicePlanType", default=None,)
	status: Optional[CloudPcStatus | str] = Field(alias="status", default=None,)
	statusDetail: Optional[CloudPcStatusDetail] = Field(alias="statusDetail", default=None,)
	statusDetails: Optional[CloudPcStatusDetails] = Field(alias="statusDetails", default=None,)
	userAccountType: Optional[CloudPcUserAccountType | str] = Field(alias="userAccountType", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)

from .cloud_pc_connection_setting import CloudPcConnectionSetting
from .cloud_pc_connection_settings import CloudPcConnectionSettings
from .cloud_pc_connectivity_result import CloudPcConnectivityResult
from .cloud_pc_disaster_recovery_capability import CloudPcDisasterRecoveryCapability
from .cloud_pc_disk_encryption_state import CloudPcDiskEncryptionState
from .frontline_cloud_pc_availability import FrontlineCloudPcAvailability
from .cloud_pc_login_result import CloudPcLoginResult
from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
from .cloud_pc_operating_system import CloudPcOperatingSystem
from .cloud_pc_partner_agent_install_result import CloudPcPartnerAgentInstallResult
from .cloud_pc_power_state import CloudPcPowerState
from .cloud_pc_product_type import CloudPcProductType
from .cloud_pc_provisioning_type import CloudPcProvisioningType
from .cloud_pc_service_plan_type import CloudPcServicePlanType
from .cloud_pc_status import CloudPcStatus
from .cloud_pc_status_detail import CloudPcStatusDetail
from .cloud_pc_status_details import CloudPcStatusDetails
from .cloud_pc_user_account_type import CloudPcUserAccountType

