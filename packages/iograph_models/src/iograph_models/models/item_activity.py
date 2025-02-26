from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ItemActivity(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	access: Optional[AccessAction] = Field(default=None,alias="access",)
	activityDateTime: Optional[datetime] = Field(default=None,alias="activityDateTime",)
	actor: Optional[IdentitySet] = Field(default=None,alias="actor",)
	driveItem: Optional[DriveItem] = Field(default=None,alias="driveItem",)

from .access_action import AccessAction
from .identity_set import IdentitySet
from .drive_item import DriveItem

