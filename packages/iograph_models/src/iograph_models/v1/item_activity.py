from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	access: Optional[AccessAction] = Field(alias="access",default=None,)
	activityDateTime: Optional[datetime] = Field(alias="activityDateTime",default=None,)
	actor: SerializeAsAny[Optional[IdentitySet]] = Field(alias="actor",default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem",default=None,)

from .access_action import AccessAction
from .identity_set import IdentitySet
from .drive_item import DriveItem

