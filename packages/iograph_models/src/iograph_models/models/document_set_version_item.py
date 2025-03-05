from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSetVersionItem(BaseModel):
	itemId: Optional[str] = Field(default=None,alias="itemId",)
	title: Optional[str] = Field(default=None,alias="title",)
	versionId: Optional[str] = Field(default=None,alias="versionId",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


