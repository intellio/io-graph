from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Add_token_signing_certificatePostRequest(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)

