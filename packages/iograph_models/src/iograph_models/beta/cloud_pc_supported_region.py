from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class CloudPcSupportedRegion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.cloudPcSupportedRegion"] = Field(alias="@odata.type",)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	regionGroup: Optional[CloudPcRegionGroup | str] = Field(alias="regionGroup", default=None,)
	regionStatus: Optional[CloudPcSupportedRegionStatus | str] = Field(alias="regionStatus", default=None,)
	supportedSolution: Optional[CloudPcManagementService | str] = Field(alias="supportedSolution", default=None,)

from .cloud_pc_region_group import CloudPcRegionGroup
from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
from .cloud_pc_management_service import CloudPcManagementService
