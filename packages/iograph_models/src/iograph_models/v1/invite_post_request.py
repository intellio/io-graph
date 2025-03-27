from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvitePostRequest(BaseModel):
	requireSignIn: Optional[bool] = Field(alias="requireSignIn", default=None,)
	roles: Optional[list[str]] = Field(alias="roles", default=None,)
	sendInvitation: Optional[bool] = Field(alias="sendInvitation", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	recipients: Optional[list[DriveRecipient]] = Field(alias="recipients", default=None,)
	retainInheritedPermissions: Optional[bool] = Field(alias="retainInheritedPermissions", default=None,)
	expirationDateTime: Optional[str] = Field(alias="expirationDateTime", default=None,)
	password: Optional[str] = Field(alias="password", default=None,)

from .drive_recipient import DriveRecipient

