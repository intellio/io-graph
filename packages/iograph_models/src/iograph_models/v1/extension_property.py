from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ExtensionProperty(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.extensionProperty"] = Field(alias="@odata.type", default="#microsoft.graph.extensionProperty")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	appDisplayName: Optional[str] = Field(alias="appDisplayName", default=None,)
	dataType: Optional[str] = Field(alias="dataType", default=None,)
	isMultiValued: Optional[bool] = Field(alias="isMultiValued", default=None,)
	isSyncedFromOnPremises: Optional[bool] = Field(alias="isSyncedFromOnPremises", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	targetObjects: Optional[list[str]] = Field(alias="targetObjects", default=None,)


