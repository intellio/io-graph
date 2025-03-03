from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcProvisioningPolicy(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	alternateResourceUrl: Optional[str] = Field(default=None,alias="alternateResourceUrl",)
	autopatch: Optional[CloudPcProvisioningPolicyAutopatch] = Field(default=None,alias="autopatch",)
	cloudPcGroupDisplayName: Optional[str] = Field(default=None,alias="cloudPcGroupDisplayName",)
	cloudPcNamingTemplate: Optional[str] = Field(default=None,alias="cloudPcNamingTemplate",)
	description: Optional[str] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	domainJoinConfigurations: Optional[list[CloudPcDomainJoinConfiguration]] = Field(default=None,alias="domainJoinConfigurations",)
	enableSingleSignOn: Optional[bool] = Field(default=None,alias="enableSingleSignOn",)
	gracePeriodInHours: Optional[int] = Field(default=None,alias="gracePeriodInHours",)
	imageDisplayName: Optional[str] = Field(default=None,alias="imageDisplayName",)
	imageId: Optional[str] = Field(default=None,alias="imageId",)
	imageType: Optional[CloudPcProvisioningPolicyImageType] = Field(default=None,alias="imageType",)
	localAdminEnabled: Optional[bool] = Field(default=None,alias="localAdminEnabled",)
	microsoftManagedDesktop: Optional[MicrosoftManagedDesktop] = Field(default=None,alias="microsoftManagedDesktop",)
	provisioningType: Optional[CloudPcProvisioningType] = Field(default=None,alias="provisioningType",)
	windowsSetting: Optional[CloudPcWindowsSetting] = Field(default=None,alias="windowsSetting",)
	assignments: Optional[list[CloudPcProvisioningPolicyAssignment]] = Field(default=None,alias="assignments",)

from .cloud_pc_provisioning_policy_autopatch import CloudPcProvisioningPolicyAutopatch
from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration
from .cloud_pc_provisioning_policy_image_type import CloudPcProvisioningPolicyImageType
from .microsoft_managed_desktop import MicrosoftManagedDesktop
from .cloud_pc_provisioning_type import CloudPcProvisioningType
from .cloud_pc_windows_setting import CloudPcWindowsSetting
from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment

