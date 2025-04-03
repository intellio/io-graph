from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MicrosoftTunnelHealthThreshold(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.microsoftTunnelHealthThreshold"] = Field(alias="@odata.type", default="#microsoft.graph.microsoftTunnelHealthThreshold")
	defaultHealthyThreshold: Optional[int] = Field(alias="defaultHealthyThreshold", default=None,)
	defaultUnhealthyThreshold: Optional[int] = Field(alias="defaultUnhealthyThreshold", default=None,)
	healthyThreshold: Optional[int] = Field(alias="healthyThreshold", default=None,)
	unhealthyThreshold: Optional[int] = Field(alias="unhealthyThreshold", default=None,)

