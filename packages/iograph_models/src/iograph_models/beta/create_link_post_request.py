from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Create_linkPostRequest(BaseModel):
	type: Optional[str] = Field(alias="type", default=None,)
	scope: Optional[str] = Field(alias="scope", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	password: Optional[str] = Field(alias="password", default=None,)
	message: Optional[str] = Field(alias="message", default=None,)
	recipients: Optional[list[DriveRecipient]] = Field(alias="recipients", default=None,)
	retainInheritedPermissions: Optional[bool] = Field(alias="retainInheritedPermissions", default=None,)
	sendNotification: Optional[bool] = Field(alias="sendNotification", default=None,)

from .drive_recipient import DriveRecipient

