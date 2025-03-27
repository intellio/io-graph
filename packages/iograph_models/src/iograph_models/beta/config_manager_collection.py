from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConfigManagerCollection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	collectionIdentifier: Optional[str] = Field(alias="collectionIdentifier", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	hierarchyIdentifier: Optional[str] = Field(alias="hierarchyIdentifier", default=None,)
	hierarchyName: Optional[str] = Field(alias="hierarchyName", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)


