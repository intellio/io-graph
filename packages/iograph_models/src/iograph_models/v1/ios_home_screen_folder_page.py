from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosHomeScreenFolderPage(BaseModel):
	apps: Optional[list[IosHomeScreenApp]] = Field(alias="apps",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .ios_home_screen_app import IosHomeScreenApp

