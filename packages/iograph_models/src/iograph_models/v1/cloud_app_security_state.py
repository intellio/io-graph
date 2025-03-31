from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudAppSecurityState(BaseModel):
	destinationServiceIp: Optional[str] = Field(alias="destinationServiceIp", default=None,)
	destinationServiceName: Optional[str] = Field(alias="destinationServiceName", default=None,)
	riskScore: Optional[str] = Field(alias="riskScore", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

