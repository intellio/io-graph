from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityDetails(BaseModel):
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	lastActiveDateTime: Optional[datetime] = Field(alias="lastActiveDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


