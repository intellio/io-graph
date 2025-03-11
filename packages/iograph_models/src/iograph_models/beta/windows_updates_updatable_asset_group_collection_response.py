from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatableAssetGroupCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsUpdatesUpdatableAssetGroup]] = Field(alias="value",default=None,)

from .windows_updates_updatable_asset_group import WindowsUpdatesUpdatableAssetGroup

