from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AuthenticationConditionApplication(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

