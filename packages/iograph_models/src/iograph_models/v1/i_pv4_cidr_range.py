from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IPv4CidrRange(BaseModel):
	odata_type: Literal["#microsoft.graph.iPv4CidrRange"] = Field(alias="@odata.type", default="#microsoft.graph.iPv4CidrRange")
	cidrAddress: Optional[str] = Field(alias="cidrAddress", default=None,)

