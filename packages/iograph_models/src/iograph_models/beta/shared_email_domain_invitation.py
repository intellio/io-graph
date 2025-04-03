from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SharedEmailDomainInvitation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.sharedEmailDomainInvitation"] = Field(alias="@odata.type", default="#microsoft.graph.sharedEmailDomainInvitation")
	expiryTime: Optional[datetime] = Field(alias="expiryTime", default=None,)
	invitationDomain: Optional[str] = Field(alias="invitationDomain", default=None,)
	invitationStatus: Optional[str] = Field(alias="invitationStatus", default=None,)

