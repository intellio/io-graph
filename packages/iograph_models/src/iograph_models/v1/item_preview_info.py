from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemPreviewInfo(BaseModel):
	getUrl: Optional[str] = Field(alias="getUrl", default=None,)
	postParameters: Optional[str] = Field(alias="postParameters", default=None,)
	postUrl: Optional[str] = Field(alias="postUrl", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


