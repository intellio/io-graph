from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenFolder(BaseModel):
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	pages: Optional[list[IosHomeScreenFolderPage]] = Field(alias="pages",default=None,)

from .ios_home_screen_folder_page import IosHomeScreenFolderPage

