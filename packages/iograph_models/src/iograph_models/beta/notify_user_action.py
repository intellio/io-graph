from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class NotifyUserAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	actionLastModifiedDateTime: Optional[datetime] = Field(alias="actionLastModifiedDateTime",default=None,)
	emailText: Optional[str] = Field(alias="emailText",default=None,)
	policyTip: Optional[str] = Field(alias="policyTip",default=None,)
	recipients: Optional[list[str]] = Field(alias="recipients",default=None,)


