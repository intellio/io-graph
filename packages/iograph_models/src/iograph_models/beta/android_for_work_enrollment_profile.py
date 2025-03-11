from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkEnrollmentProfile(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	accountId: Optional[str] = Field(alias="accountId",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[str] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	enrolledDeviceCount: Optional[int] = Field(alias="enrolledDeviceCount",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	qrCodeContent: Optional[str] = Field(alias="qrCodeContent",default=None,)
	qrCodeImage: Optional[MimeContent] = Field(alias="qrCodeImage",default=None,)
	tokenExpirationDateTime: Optional[datetime] = Field(alias="tokenExpirationDateTime",default=None,)
	tokenValue: Optional[str] = Field(alias="tokenValue",default=None,)

from .mime_content import MimeContent

