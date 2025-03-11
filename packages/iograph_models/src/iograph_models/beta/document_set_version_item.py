from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DocumentSetVersionItem(BaseModel):
	itemId: Optional[str] = Field(alias="itemId",default=None,)
	title: Optional[str] = Field(alias="title",default=None,)
	versionId: Optional[str] = Field(alias="versionId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


