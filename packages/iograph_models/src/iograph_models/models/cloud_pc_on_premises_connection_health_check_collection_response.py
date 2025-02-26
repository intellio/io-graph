from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcOnPremisesConnectionHealthCheckCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[CloudPcOnPremisesConnectionHealthCheck] = Field(alias="value",)

from .cloud_pc_on_premises_connection_health_check import CloudPcOnPremisesConnectionHealthCheck

