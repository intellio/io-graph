from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class FolderView(BaseModel):
	sortBy: Optional[str] = Field(alias="sortBy",default=None,)
	sortOrder: Optional[str] = Field(alias="sortOrder",default=None,)
	viewType: Optional[str] = Field(alias="viewType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


