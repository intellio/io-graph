from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeploymentAudience(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	applicableContent: Optional[list[WindowsUpdatesApplicableContent]] = Field(alias="applicableContent", default=None,)
	exclusions: Optional[list[Annotated[Union[WindowsUpdatesAzureADDevice, WindowsUpdatesUpdatableAssetGroup]],Field(discriminator="odata_type")]]] = Field(alias="exclusions", default=None,)
	members: Optional[list[Annotated[Union[WindowsUpdatesAzureADDevice, WindowsUpdatesUpdatableAssetGroup]],Field(discriminator="odata_type")]]] = Field(alias="members", default=None,)

from .windows_updates_applicable_content import WindowsUpdatesApplicableContent
from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup
from .windows_updates_azure_a_d_device import WindowsUpdatesAzureADDevice
from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup

