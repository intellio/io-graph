from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class UserSignInInsight(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	insightCreatedDateTime: Optional[datetime] = Field(alias="insightCreatedDateTime",default=None,)
	lastSignInDateTime: Optional[datetime] = Field(alias="lastSignInDateTime",default=None,)


