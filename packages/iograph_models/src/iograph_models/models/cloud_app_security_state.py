from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudAppSecurityState(BaseModel):
	destinationServiceIp: Optional[str] = Field(default=None,alias="destinationServiceIp",)
	destinationServiceName: Optional[str] = Field(default=None,alias="destinationServiceName",)
	riskScore: Optional[str] = Field(default=None,alias="riskScore",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


