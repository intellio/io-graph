from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MobileAppContent(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	containedApps: list[MobileContainedApp] = Field(alias="containedApps",)
	files: list[MobileAppContentFile] = Field(alias="files",)

from .mobile_contained_app import MobileContainedApp
from .mobile_app_content_file import MobileAppContentFile

