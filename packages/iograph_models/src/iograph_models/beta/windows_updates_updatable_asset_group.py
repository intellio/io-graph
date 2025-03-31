from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class WindowsUpdatesUpdatableAssetGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.windowsUpdates.updatableAssetGroup"] = Field(alias="@odata.type", default="#microsoft.graph.windowsUpdates.updatableAssetGroup")
	members: Optional[list[Annotated[Union[WindowsUpdatesAzureADDevice, WindowsUpdatesUpdatableAssetGroup],Field(discriminator="odata_type")]]] = Field(alias="members", default=None,)

from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
