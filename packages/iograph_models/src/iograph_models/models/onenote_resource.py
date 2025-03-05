from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnenoteResource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	self: Optional[str] = Field(default=None,alias="self",)
	content: Optional[str] = Field(default=None,alias="content",)
	contentUrl: Optional[str] = Field(default=None,alias="contentUrl",)


