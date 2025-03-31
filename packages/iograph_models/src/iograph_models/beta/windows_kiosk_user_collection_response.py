from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsKioskUserCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[WindowsKioskActiveDirectoryGroup, WindowsKioskAutologon, WindowsKioskAzureADGroup, WindowsKioskAzureADUser, WindowsKioskLocalGroup, WindowsKioskLocalUser, WindowsKioskVisitor],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows_kiosk_active_directory_group import WindowsKioskActiveDirectoryGroup
from .windows_kiosk_autologon import WindowsKioskAutologon
from .windows_kiosk_azure_a_d_group import WindowsKioskAzureADGroup
from .windows_kiosk_azure_a_d_user import WindowsKioskAzureADUser
from .windows_kiosk_local_group import WindowsKioskLocalGroup
from .windows_kiosk_local_user import WindowsKioskLocalUser
from .windows_kiosk_visitor import WindowsKioskVisitor
