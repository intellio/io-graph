from __future__ import annotations
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Picture(BaseModel):
	content: Optional[str] = Field(alias="content",default=None,)
	contentType: Optional[str] = Field(alias="contentType",default=None,)
	height: Optional[int] = Field(alias="height",default=None,)
	id: Optional[UUID] = Field(alias="id",default=None,)
	width: Optional[int] = Field(alias="width",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


