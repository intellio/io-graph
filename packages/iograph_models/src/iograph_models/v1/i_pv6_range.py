from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IPv6Range(BaseModel):
	odata_type: Literal["#microsoft.graph.iPv6Range"] = Field(alias="@odata.type", default="#microsoft.graph.iPv6Range")
	lowerAddress: Optional[str] = Field(alias="lowerAddress", default=None,)
	upperAddress: Optional[str] = Field(alias="upperAddress", default=None,)


