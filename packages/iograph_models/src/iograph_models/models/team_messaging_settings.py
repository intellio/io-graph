from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamMessagingSettings(BaseModel):
	allowChannelMentions: Optional[bool] = Field(default=None,alias="allowChannelMentions",)
	allowOwnerDeleteMessages: Optional[bool] = Field(default=None,alias="allowOwnerDeleteMessages",)
	allowTeamMentions: Optional[bool] = Field(default=None,alias="allowTeamMentions",)
	allowUserDeleteMessages: Optional[bool] = Field(default=None,alias="allowUserDeleteMessages",)
	allowUserEditMessages: Optional[bool] = Field(default=None,alias="allowUserEditMessages",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


