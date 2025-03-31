from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class Windows_updates_unenroll_assetsPostRequest(BaseModel):
	updateCategory: Optional[WindowsUpdatesUpdateCategory | str] = Field(alias="updateCategory", default=None,)
	assets: Optional[list[Annotated[Union[WindowsUpdatesAzureADDevice, WindowsUpdatesUpdatableAssetGroup],Field(discriminator="odata_type")]]] = Field(alias="assets", default=None,)

from .windows_updates_update_category import WindowsUpdatesUpdateCategory
from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup
