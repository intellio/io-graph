from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemPreviewInfo(BaseModel):
	getUrl: Optional[str] = Field(default=None,alias="getUrl",)
	postParameters: Optional[str] = Field(default=None,alias="postParameters",)
	postUrl: Optional[str] = Field(default=None,alias="postUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


