from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Invitation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	invitedUserDisplayName: Optional[str] = Field(alias="invitedUserDisplayName",default=None,)
	invitedUserEmailAddress: Optional[str] = Field(alias="invitedUserEmailAddress",default=None,)
	invitedUserMessageInfo: Optional[InvitedUserMessageInfo] = Field(alias="invitedUserMessageInfo",default=None,)
	invitedUserType: Optional[str] = Field(alias="invitedUserType",default=None,)
	inviteRedeemUrl: Optional[str] = Field(alias="inviteRedeemUrl",default=None,)
	inviteRedirectUrl: Optional[str] = Field(alias="inviteRedirectUrl",default=None,)
	resetRedemption: Optional[bool] = Field(alias="resetRedemption",default=None,)
	sendInvitationMessage: Optional[bool] = Field(alias="sendInvitationMessage",default=None,)
	status: Optional[str] = Field(alias="status",default=None,)
	invitedUser: Optional[User] = Field(alias="invitedUser",default=None,)
	invitedUserSponsors: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="invitedUserSponsors",default=None,)

from .invited_user_message_info import InvitedUserMessageInfo
from .user import User
from .directory_object import DirectoryObject

