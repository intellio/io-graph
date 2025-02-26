from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosHomeScreenFolderPage(BaseModel):
	apps: list[IosHomeScreenApp] = Field(alias="apps",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ios_home_screen_app import IosHomeScreenApp

