from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcDomainJoinConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcDomainJoinConfiguration] = Field(alias="value",)

from .cloud_pc_domain_join_configuration import CloudPcDomainJoinConfiguration

