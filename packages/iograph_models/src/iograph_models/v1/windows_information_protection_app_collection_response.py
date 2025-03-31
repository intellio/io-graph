from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsInformationProtectionAppCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[WindowsInformationProtectionDesktopApp, WindowsInformationProtectionStoreApp],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp
