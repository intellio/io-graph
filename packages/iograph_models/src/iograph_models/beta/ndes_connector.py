from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NdesConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.ndesConnector"] = Field(alias="@odata.type", default="#microsoft.graph.ndesConnector")
	connectorVersion: Optional[str] = Field(alias="connectorVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enrolledDateTime: Optional[datetime] = Field(alias="enrolledDateTime", default=None,)
	lastConnectionDateTime: Optional[datetime] = Field(alias="lastConnectionDateTime", default=None,)
	machineName: Optional[str] = Field(alias="machineName", default=None,)
	roleScopeTagIds: Optional[list[str]] = Field(alias="roleScopeTagIds", default=None,)
	state: Optional[NdesConnectorState | str] = Field(alias="state", default=None,)

from .ndes_connector_state import NdesConnectorState
