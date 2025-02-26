from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharepointIds(BaseModel):
	listId: Optional[str] = Field(default=None,alias="listId",)
	listItemId: Optional[str] = Field(default=None,alias="listItemId",)
	listItemUniqueId: Optional[str] = Field(default=None,alias="listItemUniqueId",)
	siteId: Optional[str] = Field(default=None,alias="siteId",)
	siteUrl: Optional[str] = Field(default=None,alias="siteUrl",)
	tenantId: Optional[str] = Field(default=None,alias="tenantId",)
	webId: Optional[str] = Field(default=None,alias="webId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


