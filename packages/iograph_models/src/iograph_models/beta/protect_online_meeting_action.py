from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ProtectOnlineMeetingAction(BaseModel):
	name: Optional[str] = Field(alias="name", default=None,)
	odata_type: Literal["#microsoft.graph.protectOnlineMeetingAction"] = Field(alias="@odata.type", default="#microsoft.graph.protectOnlineMeetingAction")
	allowedForwarders: Optional[OnlineMeetingForwarders | str] = Field(alias="allowedForwarders", default=None,)
	allowedPresenters: Optional[OnlineMeetingPresenters | str] = Field(alias="allowedPresenters", default=None,)
	isCopyToClipboardEnabled: Optional[bool] = Field(alias="isCopyToClipboardEnabled", default=None,)
	isLobbyEnabled: Optional[bool] = Field(alias="isLobbyEnabled", default=None,)
	lobbyBypassSettings: Optional[LobbyBypassSettings] = Field(alias="lobbyBypassSettings", default=None,)

from .online_meeting_forwarders import OnlineMeetingForwarders
from .online_meeting_presenters import OnlineMeetingPresenters
from .lobby_bypass_settings import LobbyBypassSettings
