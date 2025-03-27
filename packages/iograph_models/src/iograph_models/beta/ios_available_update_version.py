from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IosAvailableUpdateVersion(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	postingDateTime: Optional[datetime] = Field(alias="postingDateTime", default=None,)
	productVersion: Optional[str] = Field(alias="productVersion", default=None,)
	supportedDevices: Optional[list[str]] = Field(alias="supportedDevices", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


