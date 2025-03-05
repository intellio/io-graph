from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiedPublisher(BaseModel):
	addedDateTime: Optional[datetime] = Field(default=None,alias="addedDateTime",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	verifiedPublisherId: Optional[str] = Field(default=None,alias="verifiedPublisherId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


