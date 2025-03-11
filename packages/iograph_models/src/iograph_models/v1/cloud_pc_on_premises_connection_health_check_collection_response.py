from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcOnPremisesConnectionHealthCheckCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[CloudPcOnPremisesConnectionHealthCheck]] = Field(alias="value",default=None,)

from .cloud_pc_on_premises_connection_health_check import CloudPcOnPremisesConnectionHealthCheck

