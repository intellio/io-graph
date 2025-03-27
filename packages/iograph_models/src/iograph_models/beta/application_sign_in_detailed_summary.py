from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ApplicationSignInDetailedSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	aggregatedEventDateTime: Optional[datetime] = Field(alias="aggregatedEventDateTime", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	appId: Optional[str] = Field(alias="appId", default=None,)
	signInCount: Optional[int] = Field(alias="signInCount", default=None,)
	status: Optional[SignInStatus] = Field(alias="status", default=None,)

from .sign_in_status import SignInStatus

