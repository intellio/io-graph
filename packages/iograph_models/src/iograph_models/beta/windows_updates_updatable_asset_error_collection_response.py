from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesUpdatableAssetErrorCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAssetError]]] = Field(alias="value",default=None,)

from .windows_updates_updatable_asset_error import WindowsUpdatesUpdatableAssetError

