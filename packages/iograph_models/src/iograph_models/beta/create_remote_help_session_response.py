from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CreateRemoteHelpSessionResponse(BaseModel):
	sessionKey: Optional[str] = Field(alias="sessionKey", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

