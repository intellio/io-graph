from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class TelecomExpenseManagementPartner(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	appAuthorized: Optional[bool] = Field(alias="appAuthorized", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	enabled: Optional[bool] = Field(alias="enabled", default=None,)
	lastConnectionDateTime: Optional[datetime] = Field(alias="lastConnectionDateTime", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)


