from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class MobileAppContent(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	containedApps: Optional[list[Annotated[Union[MicrosoftStoreForBusinessContainedApp, WindowsUniversalAppXContainedApp]],Field(discriminator="odata_type")]]] = Field(alias="containedApps", default=None,)
	files: Optional[list[MobileAppContentFile]] = Field(alias="files", default=None,)

from .microsoft_store_for_business_contained_app import MicrosoftStoreForBusinessContainedApp
from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
from .mobile_app_content_file import MobileAppContentFile

