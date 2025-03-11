from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows_updates_enroll_assetsPostRequest(BaseModel):
	updateCategory: Optional[WindowsUpdatesUpdateCategory | str] = Field(alias="updateCategory",default=None,)
	assets: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="assets",default=None,)

from .windows_updates_update_category import WindowsUpdatesUpdateCategory
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset

