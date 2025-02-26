from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ExtensionProperty(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	appDisplayName: Optional[str] = Field(default=None,alias="appDisplayName",)
	dataType: Optional[str] = Field(default=None,alias="dataType",)
	isMultiValued: Optional[bool] = Field(default=None,alias="isMultiValued",)
	isSyncedFromOnPremises: Optional[bool] = Field(default=None,alias="isSyncedFromOnPremises",)
	name: Optional[str] = Field(default=None,alias="name",)
	targetObjects: list[str] = Field(alias="targetObjects",)


