from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosHomeScreenPage(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	icons: Optional[list[IosHomeScreenItem]] = Field(default=None,alias="icons",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ios_home_screen_item import IosHomeScreenItem

