from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class IPv4Range(BaseModel):
	odata_type: Literal["#microsoft.graph.iPv4Range"] = Field(alias="@odata.type", default="#microsoft.graph.iPv4Range")
	lowerAddress: Optional[str] = Field(alias="lowerAddress", default=None,)
	upperAddress: Optional[str] = Field(alias="upperAddress", default=None,)

