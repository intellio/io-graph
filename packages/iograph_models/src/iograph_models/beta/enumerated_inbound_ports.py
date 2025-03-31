from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EnumeratedInboundPorts(BaseModel):
	odata_type: Literal["#microsoft.graph.enumeratedInboundPorts"] = Field(alias="@odata.type", default="#microsoft.graph.enumeratedInboundPorts")
	ports: Optional[list[str]] = Field(alias="ports", default=None,)

