from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharepointIds(BaseModel):
	listId: Optional[str] = Field(alias="listId",default=None,)
	listItemId: Optional[str] = Field(alias="listItemId",default=None,)
	listItemUniqueId: Optional[str] = Field(alias="listItemUniqueId",default=None,)
	siteId: Optional[str] = Field(alias="siteId",default=None,)
	siteUrl: Optional[str] = Field(alias="siteUrl",default=None,)
	tenantId: Optional[str] = Field(alias="tenantId",default=None,)
	webId: Optional[str] = Field(alias="webId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


