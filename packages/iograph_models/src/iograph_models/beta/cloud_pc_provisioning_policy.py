from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcProvisioningPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcProvisioningPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcProvisioningPolicy")
	alternateResourceUrl: Optional[str] = Field(alias="alternateResourceUrl", default=None,)
	autopatch: Optional[CloudPcProvisioningPolicyAutopatch] = Field(alias="autopatch", default=None,)
	autopilotConfiguration: Optional[CloudPcAutopilotConfiguration] = Field(alias="autopilotConfiguration", default=None,)
	cloudPcGroupDisplayName: Optional[str] = Field(alias="cloudPcGroupDisplayName", default=None,)
	cloudPcNamingTemplate: Optional[str] = Field(alias="cloudPcNamingTemplate", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	domainJoinConfigurations: Optional[list[CloudPcDomainJoinConfiguration]] = Field(alias="domainJoinConfigurations", default=None,)
	enableSingleSignOn: Optional[bool] = Field(alias="enableSingleSignOn", default=None,)
	gracePeriodInHours: Optional[int] = Field(alias="gracePeriodInHours", default=None,)
	imageDisplayName: Optional[str] = Field(alias="imageDisplayName", default=None,)
	imageId: Optional[str] = Field(alias="imageId", default=None,)
	imageType: Optional[CloudPcProvisioningPolicyImageType | str] = Field(alias="imageType", default=None,)
	localAdminEnabled: Optional[bool] = Field(alias="localAdminEnabled", default=None,)
	managedBy: Optional[CloudPcManagementService | str] = Field(alias="managedBy", default=None,)
	microsoftManagedDesktop: Optional[MicrosoftManagedDesktop] = Field(alias="microsoftManagedDesktop", default=None,)
	provisioningType: Optional[CloudPcProvisioningType | str] = Field(alias="provisioningType", default=None,)
	scopeIds: Optional[list[str]] = Field(alias="scopeIds", default=None,)
	windowsSetting: Optional[CloudPcWindowsSetting] = Field(alias="windowsSetting", default=None,)
	windowsSettings: Optional[CloudPcWindowsSettings] = Field(alias="windowsSettings", default=None,)
	assignments: Optional[list[CloudPcProvisioningPolicyAssignment]] = Field(alias="assignments", default=None,)

from .cloud_pc_provisioning_policy_autopatch import CloudPcProvisioningPolicyAutopatch
from .cloud_pc_autopilot_configuration import CloudPcAutopilotConfiguration
from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
from .cloud_pc_management_service import CloudPcManagementService
from .microsoft_managed_desktop import MicrosoftManagedDesktop
from .cloud_pc_provisioning_type import CloudPcProvisioningType
from .cloud_pc_windows_setting import CloudPcWindowsSetting
from .cloud_pc_windows_settings import CloudPcWindowsSettings
from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
