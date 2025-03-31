from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharingLinkExpirationStatus(BaseModel):
	defaultExpirationInDays: Optional[int] = Field(alias="defaultExpirationInDays", default=None,)
	disabledReason: Optional[str] = Field(alias="disabledReason", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

