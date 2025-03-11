from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AllowedDataLocation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	appId: Optional[str] = Field(alias="appId",default=None,)
	domain: Optional[str] = Field(alias="domain",default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault",default=None,)
	location: Optional[str] = Field(alias="location",default=None,)


