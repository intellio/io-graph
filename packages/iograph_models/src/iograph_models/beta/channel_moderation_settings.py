from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ChannelModerationSettings(BaseModel):
	allowNewMessageFromBots: Optional[bool] = Field(alias="allowNewMessageFromBots", default=None,)
	allowNewMessageFromConnectors: Optional[bool] = Field(alias="allowNewMessageFromConnectors", default=None,)
	replyRestriction: Optional[ReplyRestriction | str] = Field(alias="replyRestriction", default=None,)
	userNewMessageRestriction: Optional[UserNewMessageRestriction | str] = Field(alias="userNewMessageRestriction", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .reply_restriction import ReplyRestriction
from .user_new_message_restriction import UserNewMessageRestriction
