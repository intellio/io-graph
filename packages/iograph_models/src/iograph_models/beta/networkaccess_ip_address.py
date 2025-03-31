from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessIpAddress(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.ipAddress"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.ipAddress")
	value: Optional[str] = Field(alias="value", default=None,)

