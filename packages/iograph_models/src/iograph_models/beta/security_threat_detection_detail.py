from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityThreatDetectionDetail(BaseModel):
	confidenceLevel: Optional[str] = Field(alias="confidenceLevel",default=None,)
	priorityAccountProtection: Optional[str] = Field(alias="priorityAccountProtection",default=None,)
	threats: Optional[str] = Field(alias="threats",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


