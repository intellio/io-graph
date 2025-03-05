from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenPage(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	icons: SerializeAsAny[Optional[list[IosHomeScreenItem]]] = Field(default=None,alias="icons",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ios_home_screen_item import IosHomeScreenItem

