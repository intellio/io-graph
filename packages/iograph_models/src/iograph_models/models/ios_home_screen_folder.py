from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IosHomeScreenFolder(BaseModel):
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	pages: Optional[list[IosHomeScreenFolderPage]] = Field(default=None,alias="pages",)

from .ios_home_screen_folder_page import IosHomeScreenFolderPage

