from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesDeploymentAudience(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicableContent: Optional[list[WindowsUpdatesApplicableContent]] = Field(alias="applicableContent",default=None,)
	exclusions: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="exclusions",default=None,)
	members: SerializeAsAny[Optional[list[WindowsUpdatesUpdatableAsset]]] = Field(alias="members",default=None,)

from .windows_updates_applicable_content import WindowsUpdatesApplicableContent
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset
from .windows_updates_updatable_asset import WindowsUpdatesUpdatableAsset

