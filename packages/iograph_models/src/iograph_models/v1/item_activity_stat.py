from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ItemActivityStat(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.itemActivityStat"] = Field(alias="@odata.type",)
	access: Optional[ItemActionStat] = Field(alias="access", default=None,)
	create: Optional[ItemActionStat] = Field(alias="create", default=None,)
	delete: Optional[ItemActionStat] = Field(alias="delete", default=None,)
	edit: Optional[ItemActionStat] = Field(alias="edit", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	incompleteData: Optional[IncompleteData] = Field(alias="incompleteData", default=None,)
	isTrending: Optional[bool] = Field(alias="isTrending", default=None,)
	move: Optional[ItemActionStat] = Field(alias="move", default=None,)
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	activities: Optional[list[ItemActivity]] = Field(alias="activities", default=None,)

from .item_action_stat import ItemActionStat
from .incomplete_data import IncompleteData
from .item_activity import ItemActivity
