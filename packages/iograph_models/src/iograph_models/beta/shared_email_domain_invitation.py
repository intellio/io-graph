from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SharedEmailDomainInvitation(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	expiryTime: Optional[datetime] = Field(alias="expiryTime",default=None,)
	invitationDomain: Optional[str] = Field(alias="invitationDomain",default=None,)
	invitationStatus: Optional[str] = Field(alias="invitationStatus",default=None,)


