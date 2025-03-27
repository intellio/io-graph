from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTunnelHealthThreshold(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	defaultHealthyThreshold: Optional[int] = Field(alias="defaultHealthyThreshold", default=None,)
	defaultUnhealthyThreshold: Optional[int] = Field(alias="defaultUnhealthyThreshold", default=None,)
	healthyThreshold: Optional[int] = Field(alias="healthyThreshold", default=None,)
	unhealthyThreshold: Optional[int] = Field(alias="unhealthyThreshold", default=None,)


