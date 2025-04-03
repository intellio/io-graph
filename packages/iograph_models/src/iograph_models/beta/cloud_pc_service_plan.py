from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcServicePlan(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcServicePlan"] = Field(alias="@odata.type", default="#microsoft.graph.cloudPcServicePlan")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	provisioningType: Optional[CloudPcProvisioningType | str] = Field(alias="provisioningType", default=None,)
	ramInGB: Optional[int] = Field(alias="ramInGB", default=None,)
	storageInGB: Optional[int] = Field(alias="storageInGB", default=None,)
	supportedSolution: Optional[CloudPcManagementService | str] = Field(alias="supportedSolution", default=None,)
	type: Optional[CloudPcServicePlanType | str] = Field(alias="type", default=None,)
	userProfileInGB: Optional[int] = Field(alias="userProfileInGB", default=None,)
	vCpuCount: Optional[int] = Field(alias="vCpuCount", default=None,)

from .cloud_pc_provisioning_type import CloudPcProvisioningType
from .cloud_pc_management_service import CloudPcManagementService
from .cloud_pc_service_plan_type import CloudPcServicePlanType
