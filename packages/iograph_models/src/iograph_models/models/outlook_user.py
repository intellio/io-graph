from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OutlookUser(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	masterCategories: Optional[list[OutlookCategory]] = Field(default=None,alias="masterCategories",)

from .outlook_category import OutlookCategory

