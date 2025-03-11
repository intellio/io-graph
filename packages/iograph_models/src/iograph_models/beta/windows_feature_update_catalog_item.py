from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsFeatureUpdateCatalogItem(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	endOfSupportDate: Optional[datetime] = Field(alias="endOfSupportDate",default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime",default=None,)
	version: Optional[str] = Field(alias="version",default=None,)


