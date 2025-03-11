from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActivityOLD(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	action: Optional[ItemActionSet] = Field(alias="action",default=None,)
	actor: SerializeAsAny[Optional[IdentitySet]] = Field(alias="actor",default=None,)
	times: Optional[ItemActivityTimeSet] = Field(alias="times",default=None,)
	driveItem: Optional[DriveItem] = Field(alias="driveItem",default=None,)
	listItem: Optional[ListItem] = Field(alias="listItem",default=None,)

from .item_action_set import ItemActionSet
from .identity_set import IdentitySet
from .item_activity_time_set import ItemActivityTimeSet
from .drive_item import DriveItem
from .list_item import ListItem

