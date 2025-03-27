from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class JoinMeetingIdMeetingInfo(BaseModel):
	allowConversationWithoutHost: Optional[bool] = Field(alias="allowConversationWithoutHost", default=None,)
	odata_type: Literal["#microsoft.graph.joinMeetingIdMeetingInfo"] = Field(alias="@odata.type", default="#microsoft.graph.joinMeetingIdMeetingInfo")
	joinMeetingId: Optional[str] = Field(alias="joinMeetingId", default=None,)
	passcode: Optional[str] = Field(alias="passcode", default=None,)


