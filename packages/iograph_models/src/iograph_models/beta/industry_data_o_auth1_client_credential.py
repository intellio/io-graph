from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOAuth1ClientCredential(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isValid: Optional[bool] = Field(alias="isValid",default=None,)
	lastValidDateTime: Optional[datetime] = Field(alias="lastValidDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	clientId: Optional[str] = Field(alias="clientId",default=None,)
	clientSecret: Optional[str] = Field(alias="clientSecret",default=None,)


