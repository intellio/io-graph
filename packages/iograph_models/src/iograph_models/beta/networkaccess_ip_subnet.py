from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class NetworkaccessIpSubnet(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.ipSubnet"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.ipSubnet")
	value: Optional[str] = Field(alias="value", default=None,)

