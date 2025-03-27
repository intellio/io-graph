from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OutlookCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	color: Optional[CategoryColor | str] = Field(alias="color", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .category_color import CategoryColor

