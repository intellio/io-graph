from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ItemActivityStat(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	access: Optional[ItemActionStat] = Field(default=None,alias="access",)
	create: Optional[ItemActionStat] = Field(default=None,alias="create",)
	delete: Optional[ItemActionStat] = Field(default=None,alias="delete",)
	edit: Optional[ItemActionStat] = Field(default=None,alias="edit",)
	endDateTime: Optional[datetime] = Field(default=None,alias="endDateTime",)
	incompleteData: Optional[IncompleteData] = Field(default=None,alias="incompleteData",)
	isTrending: Optional[bool] = Field(default=None,alias="isTrending",)
	move: Optional[ItemActionStat] = Field(default=None,alias="move",)
	startDateTime: Optional[datetime] = Field(default=None,alias="startDateTime",)
	activities: Optional[list[ItemActivity]] = Field(default=None,alias="activities",)

from .item_action_stat import ItemActionStat
from .item_action_stat import ItemActionStat
from .item_action_stat import ItemActionStat
from .item_action_stat import ItemActionStat
from .incomplete_data import IncompleteData
from .item_action_stat import ItemActionStat
from .item_activity import ItemActivity

