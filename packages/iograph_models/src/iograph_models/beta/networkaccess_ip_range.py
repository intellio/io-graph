from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class NetworkaccessIpRange(BaseModel):
	odata_type: Literal["#microsoft.graph.networkaccess.ipRange"] = Field(alias="@odata.type", default="#microsoft.graph.networkaccess.ipRange")
	beginAddress: Optional[str] = Field(alias="beginAddress", default=None,)
	endAddress: Optional[str] = Field(alias="endAddress", default=None,)


