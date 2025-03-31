from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class RemoteAssistanceSettings(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.remoteAssistanceSettings"] = Field(alias="@odata.type",)
	allowSessionsToUnenrolledDevices: Optional[bool] = Field(alias="allowSessionsToUnenrolledDevices", default=None,)
	blockChat: Optional[bool] = Field(alias="blockChat", default=None,)
	remoteAssistanceState: Optional[RemoteAssistanceState | str] = Field(alias="remoteAssistanceState", default=None,)

from .remote_assistance_state import RemoteAssistanceState
