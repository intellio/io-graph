from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AppListItem(BaseModel):
	appId: Optional[str] = Field(default=None,alias="appId",)
	appStoreUrl: Optional[str] = Field(default=None,alias="appStoreUrl",)
	name: Optional[str] = Field(default=None,alias="name",)
	publisher: Optional[str] = Field(default=None,alias="publisher",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


