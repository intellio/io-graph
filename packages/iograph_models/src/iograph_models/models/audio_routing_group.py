from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AudioRoutingGroup(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	receivers: list[Optional[str]] = Field(alias="receivers",)
	routingMode: Optional[RoutingMode] = Field(default=None,alias="routingMode",)
	sources: list[Optional[str]] = Field(alias="sources",)

from .routing_mode import RoutingMode

