from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserSignInInsight(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	insightCreatedDateTime: Optional[datetime] = Field(default=None,alias="insightCreatedDateTime",)
	lastSignInDateTime: Optional[datetime] = Field(default=None,alias="lastSignInDateTime",)


