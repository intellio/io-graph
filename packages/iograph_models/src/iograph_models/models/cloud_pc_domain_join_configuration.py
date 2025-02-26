from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcDomainJoinConfiguration(BaseModel):
	domainJoinType: Optional[CloudPcDomainJoinType] = Field(default=None,alias="domainJoinType",)
	onPremisesConnectionId: Optional[str] = Field(default=None,alias="onPremisesConnectionId",)
	regionGroup: Optional[CloudPcRegionGroup] = Field(default=None,alias="regionGroup",)
	regionName: Optional[str] = Field(default=None,alias="regionName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .cloud_pc_domain_join_type import CloudPcDomainJoinType
from .cloud_pc_region_group import CloudPcRegionGroup

