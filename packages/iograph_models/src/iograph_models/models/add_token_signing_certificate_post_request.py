from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Add_token_signing_certificatePostRequest(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)


