from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ProtectOnlineMeetingAction(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	allowedForwarders: Optional[OnlineMeetingForwarders | str] = Field(alias="allowedForwarders",default=None,)
	allowedPresenters: Optional[OnlineMeetingPresenters | str] = Field(alias="allowedPresenters",default=None,)
	isCopyToClipboardEnabled: Optional[bool] = Field(alias="isCopyToClipboardEnabled",default=None,)
	isLobbyEnabled: Optional[bool] = Field(alias="isLobbyEnabled",default=None,)
	lobbyBypassSettings: Optional[LobbyBypassSettings] = Field(alias="lobbyBypassSettings",default=None,)

from .online_meeting_forwarders import OnlineMeetingForwarders
from .online_meeting_presenters import OnlineMeetingPresenters
from .lobby_bypass_settings import LobbyBypassSettings

