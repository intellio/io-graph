from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TicketInfo(BaseModel):
	ticketApproverIdentityId: Optional[str] = Field(alias="ticketApproverIdentityId",default=None,)
	ticketNumber: Optional[str] = Field(alias="ticketNumber",default=None,)
	ticketSubmitterIdentityId: Optional[str] = Field(alias="ticketSubmitterIdentityId",default=None,)
	ticketSystem: Optional[str] = Field(alias="ticketSystem",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


