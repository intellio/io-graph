from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RequestActivity(BaseModel):
	action: Optional[str] = Field(alias="action", default=None,)
	actionDateTime: Optional[datetime] = Field(alias="actionDateTime", default=None,)
	detail: Optional[str] = Field(alias="detail", default=None,)
	scheduledDateTime: Optional[datetime] = Field(alias="scheduledDateTime", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

