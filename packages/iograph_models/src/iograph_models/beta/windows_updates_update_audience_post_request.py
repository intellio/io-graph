from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows_updates_update_audiencePostRequest(BaseModel):
	addMembers: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="addMembers",default=None,)
	removeMembers: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="removeMembers",default=None,)
	addExclusions: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="addExclusions",default=None,)
	removeExclusions: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="removeExclusions",default=None,)

from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset

