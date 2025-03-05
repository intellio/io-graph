from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppContent(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	containedApps: SerializeAsAny[Optional[list[MobileContainedApp]]] = Field(alias="containedApps",default=None,)
	files: Optional[list[MobileAppContentFile]] = Field(alias="files",default=None,)

from .mobile_contained_app import MobileContainedApp
from .mobile_app_content_file import MobileAppContentFile

