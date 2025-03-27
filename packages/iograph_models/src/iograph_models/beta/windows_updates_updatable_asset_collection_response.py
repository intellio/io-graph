from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatableAssetCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[WindowsUpdatesAzureADDevice, WindowsUpdatesUpdatableAssetGroup]],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup

