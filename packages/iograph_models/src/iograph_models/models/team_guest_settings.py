from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamGuestSettings(BaseModel):
	allowCreateUpdateChannels: Optional[bool] = Field(default=None,alias="allowCreateUpdateChannels",)
	allowDeleteChannels: Optional[bool] = Field(default=None,alias="allowDeleteChannels",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


