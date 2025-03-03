from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Invitation(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	invitedUserDisplayName: Optional[str] = Field(default=None,alias="invitedUserDisplayName",)
	invitedUserEmailAddress: Optional[str] = Field(default=None,alias="invitedUserEmailAddress",)
	invitedUserMessageInfo: Optional[InvitedUserMessageInfo] = Field(default=None,alias="invitedUserMessageInfo",)
	invitedUserType: Optional[str] = Field(default=None,alias="invitedUserType",)
	inviteRedeemUrl: Optional[str] = Field(default=None,alias="inviteRedeemUrl",)
	inviteRedirectUrl: Optional[str] = Field(default=None,alias="inviteRedirectUrl",)
	resetRedemption: Optional[bool] = Field(default=None,alias="resetRedemption",)
	sendInvitationMessage: Optional[bool] = Field(default=None,alias="sendInvitationMessage",)
	status: Optional[str] = Field(default=None,alias="status",)
	invitedUser: Optional[User] = Field(default=None,alias="invitedUser",)
	invitedUserSponsors: Optional[list[DirectoryObject]] = Field(default=None,alias="invitedUserSponsors",)

from .invited_user_message_info import InvitedUserMessageInfo
from .user import User
from .directory_object import DirectoryObject

