from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcDomainJoinConfiguration(BaseModel):
	domainJoinType: Optional[CloudPcDomainJoinType | str] = Field(alias="domainJoinType", default=None,)
	onPremisesConnectionId: Optional[str] = Field(alias="onPremisesConnectionId", default=None,)
	regionGroup: Optional[CloudPcRegionGroup | str] = Field(alias="regionGroup", default=None,)
	regionName: Optional[str] = Field(alias="regionName", default=None,)
	type: Optional[CloudPcDomainJoinType | str] = Field(alias="type", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .cloud_pc_domain_join_type import CloudPcDomainJoinType
from .cloud_pc_region_group import CloudPcRegionGroup
from .cloud_pc_domain_join_type import CloudPcDomainJoinType

