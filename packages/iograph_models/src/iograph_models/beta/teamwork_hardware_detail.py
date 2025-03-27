from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkHardwareDetail(BaseModel):
	macAddresses: Optional[list[str]] = Field(alias="macAddresses", default=None,)
	manufacturer: Optional[str] = Field(alias="manufacturer", default=None,)
	model: Optional[str] = Field(alias="model", default=None,)
	serialNumber: Optional[str] = Field(alias="serialNumber", default=None,)
	uniqueId: Optional[str] = Field(alias="uniqueId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


