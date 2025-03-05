from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamGuestSettings(BaseModel):
	allowCreateUpdateChannels: Optional[bool] = Field(alias="allowCreateUpdateChannels",default=None,)
	allowDeleteChannels: Optional[bool] = Field(alias="allowDeleteChannels",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


