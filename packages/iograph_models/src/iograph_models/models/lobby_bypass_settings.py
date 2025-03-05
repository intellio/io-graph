from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LobbyBypassSettings(BaseModel):
	isDialInBypassEnabled: Optional[bool] = Field(default=None,alias="isDialInBypassEnabled",)
	scope: Optional[LobbyBypassScope] = Field(default=None,alias="scope",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .lobby_bypass_scope import LobbyBypassScope

