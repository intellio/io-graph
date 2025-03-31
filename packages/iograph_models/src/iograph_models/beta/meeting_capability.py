from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class MeetingCapability(BaseModel):
	allowAnonymousUsersToDialOut: Optional[bool] = Field(alias="allowAnonymousUsersToDialOut", default=None,)
	allowAnonymousUsersToStartMeeting: Optional[bool] = Field(alias="allowAnonymousUsersToStartMeeting", default=None,)
	autoAdmittedUsers: Optional[AutoAdmittedUsersType | str] = Field(alias="autoAdmittedUsers", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .auto_admitted_users_type import AutoAdmittedUsersType
