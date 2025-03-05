from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvitePostRequest(BaseModel):
	requireSignIn: Optional[bool] = Field(default=None,alias="requireSignIn",)
	roles: Optional[list[str]] = Field(default=None,alias="roles",)
	sendInvitation: Optional[bool] = Field(default=None,alias="sendInvitation",)
	message: Optional[str] = Field(default=None,alias="message",)
	recipients: Optional[list[DriveRecipient]] = Field(default=None,alias="recipients",)
	retainInheritedPermissions: Optional[bool] = Field(default=None,alias="retainInheritedPermissions",)
	expirationDateTime: Optional[str] = Field(default=None,alias="expirationDateTime",)
	password: Optional[str] = Field(default=None,alias="password",)

from .drive_recipient import DriveRecipient

