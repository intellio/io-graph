from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataReferenceDefinition(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	code: Optional[str] = Field(alias="code", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isDisabled: Optional[bool] = Field(alias="isDisabled", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	referenceType: Optional[str] = Field(alias="referenceType", default=None,)
	sortIndex: Optional[int] = Field(alias="sortIndex", default=None,)
	source: Optional[str] = Field(alias="source", default=None,)


