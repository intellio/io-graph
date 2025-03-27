from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AudioRoutingGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	receivers: Optional[list[str]] = Field(alias="receivers", default=None,)
	routingMode: Optional[RoutingMode | str] = Field(alias="routingMode", default=None,)
	sources: Optional[list[str]] = Field(alias="sources", default=None,)

from .routing_mode import RoutingMode

