from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class LobbyBypassSettings(BaseModel):
	isDialInBypassEnabled: Optional[bool] = Field(alias="isDialInBypassEnabled", default=None,)
	scope: Optional[LobbyBypassScope | str] = Field(alias="scope", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .lobby_bypass_scope import LobbyBypassScope
