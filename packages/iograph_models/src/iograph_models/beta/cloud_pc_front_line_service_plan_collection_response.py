from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcFrontLineServicePlanCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcFrontLineServicePlan]] = Field(alias="value", default=None,)

from .cloud_pc_front_line_service_plan import CloudPcFrontLineServicePlan

