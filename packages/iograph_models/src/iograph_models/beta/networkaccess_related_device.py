from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessRelatedDevice(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.relatedDevice"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.relatedDevice")
	deviceId: Optional[str] = Field(alias="deviceId", default=None,)

