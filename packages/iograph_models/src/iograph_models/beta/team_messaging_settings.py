from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamMessagingSettings(BaseModel):
	allowChannelMentions: Optional[bool] = Field(alias="allowChannelMentions", default=None,)
	allowOwnerDeleteMessages: Optional[bool] = Field(alias="allowOwnerDeleteMessages", default=None,)
	allowTeamMentions: Optional[bool] = Field(alias="allowTeamMentions", default=None,)
	allowUserDeleteMessages: Optional[bool] = Field(alias="allowUserDeleteMessages", default=None,)
	allowUserEditMessages: Optional[bool] = Field(alias="allowUserEditMessages", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


