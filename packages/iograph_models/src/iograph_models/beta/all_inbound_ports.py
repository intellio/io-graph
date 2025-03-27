from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AllInboundPorts(BaseModel):
	odata_type: Literal["#microsoft.graph.allInboundPorts"] = Field(alias="@odata.type", default="#microsoft.graph.allInboundPorts")


