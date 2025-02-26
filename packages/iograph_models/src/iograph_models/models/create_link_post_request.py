from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Create_linkPostRequest(BaseModel):
	type: Optional[str] = Field(default=None,alias="type",)
	scope: Optional[str] = Field(default=None,alias="scope",)
	expirationDateTime: Optional[datetime] = Field(default=None,alias="expirationDateTime",)
	password: Optional[str] = Field(default=None,alias="password",)
	message: Optional[str] = Field(default=None,alias="message",)
	recipients: list[DriveRecipient] = Field(alias="recipients",)
	retainInheritedPermissions: Optional[bool] = Field(default=None,alias="retainInheritedPermissions",)
	sendNotification: Optional[bool] = Field(default=None,alias="sendNotification",)

from .drive_recipient import DriveRecipient

