from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcSupportedRegion(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	regionGroup: Optional[CloudPcRegionGroup | str] = Field(alias="regionGroup",default=None,)
	regionStatus: Optional[CloudPcSupportedRegionStatus | str] = Field(alias="regionStatus",default=None,)
	supportedSolution: Optional[CloudPcManagementService | str] = Field(alias="supportedSolution",default=None,)

from .cloud_pc_region_group import CloudPcRegionGroup
from .cloud_pc_supported_region_status import CloudPcSupportedRegionStatus
from .cloud_pc_management_service import CloudPcManagementService

