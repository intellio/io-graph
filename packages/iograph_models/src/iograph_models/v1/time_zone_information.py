from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TimeZoneInformation(BaseModel):
	alias: Optional[str] = Field(alias="alias", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


