from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows_updates_add_membersPostRequest(BaseModel):
	assets: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="assets",default=None,)

from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset

