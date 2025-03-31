from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class IndustryDataFileUploadSession(BaseModel):
	containerExpirationDateTime: Optional[datetime] = Field(alias="containerExpirationDateTime", default=None,)
	containerId: Optional[str] = Field(alias="containerId", default=None,)
	sessionExpirationDateTime: Optional[datetime] = Field(alias="sessionExpirationDateTime", default=None,)
	sessionUrl: Optional[str] = Field(alias="sessionUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

