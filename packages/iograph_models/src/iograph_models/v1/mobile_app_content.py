from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class MobileAppContent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mobileAppContent"] = Field(alias="@odata.type", default="#microsoft.graph.mobileAppContent")
	containedApps: Optional[list[Annotated[Union[WindowsUniversalAppXContainedApp],Field(discriminator="odata_type")]]] = Field(alias="containedApps", default=None,)
	files: Optional[list[MobileAppContentFile]] = Field(alias="files", default=None,)

from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
from .mobile_app_content_file import MobileAppContentFile
