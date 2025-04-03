from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Connector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.connector"] = Field(alias="@odata.type", default="#microsoft.graph.connector")
	externalIp: Optional[str] = Field(alias="externalIp", default=None,)
	machineName: Optional[str] = Field(alias="machineName", default=None,)
	status: Optional[ConnectorStatus | str] = Field(alias="status", default=None,)
	version: Optional[str] = Field(alias="version", default=None,)
	memberOf: Optional[list[ConnectorGroup]] = Field(alias="memberOf", default=None,)

from .connector_status import ConnectorStatus
from .connector_group import ConnectorGroup
