from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OutlookCategory(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.outlookCategory"] = Field(alias="@odata.type", default="#microsoft.graph.outlookCategory")
	color: Optional[CategoryColor | str] = Field(alias="color", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)

from .category_color import CategoryColor
