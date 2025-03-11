from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExtensionProperty(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime",default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName",default=None,)
	dataType: Optional[str] = Field(alias="dataType",default=None,)
	isMultiValued: Optional[bool] = Field(alias="isMultiValued",default=None,)
	isSyncedFromOnPremises: Optional[bool] = Field(alias="isSyncedFromOnPremises",default=None,)
	name: Optional[str] = Field(alias="name",default=None,)
	targetObjects: Optional[list[str]] = Field(alias="targetObjects",default=None,)


