from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class OutlookUser(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.outlookUser"] = Field(alias="@odata.type",)
	masterCategories: Optional[list[OutlookCategory]] = Field(alias="masterCategories", default=None,)

from .outlook_category import OutlookCategory
