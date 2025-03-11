from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class MailboxItemImportSession(BaseModel):
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime",default=None,)
	importUrl: Optional[str] = Field(alias="importUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


