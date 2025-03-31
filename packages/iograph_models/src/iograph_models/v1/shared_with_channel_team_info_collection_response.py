from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SharedWithChannelTeamInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SharedWithChannelTeamInfo]] = Field(alias="value", default=None,)

from .shared_with_channel_team_info import SharedWithChannelTeamInfo
