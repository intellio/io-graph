from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class VerifiedPublisher(BaseModel):
	addedDateTime: Optional[datetime] = Field(alias="addedDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	verifiedPublisherId: Optional[str] = Field(alias="verifiedPublisherId", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


