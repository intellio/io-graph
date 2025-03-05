from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Thumbnail(BaseModel):
	content: Optional[str] = Field(alias="content",default=None,)
	height: Optional[int] = Field(alias="height",default=None,)
	sourceItemId: Optional[str] = Field(alias="sourceItemId",default=None,)
	url: Optional[str] = Field(alias="url",default=None,)
	width: Optional[int] = Field(alias="width",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


