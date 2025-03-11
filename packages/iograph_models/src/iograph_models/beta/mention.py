from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Mention(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	application: Optional[str] = Field(alias="application",default=None,)
	clientReference: Optional[str] = Field(alias="clientReference",default=None,)
	createdBy: SerializeAsAny[Optional[EmailAddress]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	deepLink: Optional[str] = Field(alias="deepLink",default=None,)
	mentioned: SerializeAsAny[Optional[EmailAddress]] = Field(alias="mentioned",default=None,)
	mentionText: Optional[str] = Field(alias="mentionText",default=None,)
	serverCreatedDateTime: Optional[datetime] = Field(alias="serverCreatedDateTime",default=None,)

from .email_address import EmailAddress
from .email_address import EmailAddress

