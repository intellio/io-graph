from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AppleAppListItem(BaseModel):
	appId: Optional[str] = Field(alias="appId", default=None,)
	appStoreUrl: Optional[str] = Field(alias="appStoreUrl", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	publisher: Optional[str] = Field(alias="publisher", default=None,)
	odata_type: Literal["#microsoft.graph.appleAppListItem"] = Field(alias="@odata.type", default="#microsoft.graph.appleAppListItem")


