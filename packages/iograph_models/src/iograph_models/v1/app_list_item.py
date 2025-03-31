from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AppListItem(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

