from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_office365_groups_activity_group_counts_with_periodGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Office365GroupsActivityGroupCounts]] = Field(alias="value", default=None,)

from .office365_groups_activity_group_counts import Office365GroupsActivityGroupCounts
