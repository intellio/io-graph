from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AudioRoutingGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	receivers: Optional[list[str]] = Field(default=None,alias="receivers",)
	routingMode: Optional[RoutingMode] = Field(default=None,alias="routingMode",)
	sources: Optional[list[str]] = Field(default=None,alias="sources",)

from .routing_mode import RoutingMode

