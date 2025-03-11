from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatableAssetGroup(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	members: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="members",default=None,)

from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset

