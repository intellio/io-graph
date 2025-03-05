from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenFolderPage(BaseModel):
	apps: Optional[list[IosHomeScreenApp]] = Field(default=None,alias="apps",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .ios_home_screen_app import IosHomeScreenApp

