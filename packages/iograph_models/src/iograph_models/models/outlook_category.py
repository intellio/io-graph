from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookCategory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	color: Optional[CategoryColor] = Field(default=None,alias="color",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)

from .category_color import CategoryColor

