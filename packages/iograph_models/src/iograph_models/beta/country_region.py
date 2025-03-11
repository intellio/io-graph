from __future__ import annotations
from uuid import UUID
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class CountryRegion(BaseModel):
	addressFormat: Optional[str] = Field(alias="addressFormat",default=None,)
	code: Optional[str] = Field(alias="code",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


