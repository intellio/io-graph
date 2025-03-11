from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharedEmailDomainInvitationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[SharedEmailDomainInvitation]] = Field(alias="value",default=None,)

from .shared_email_domain_invitation import SharedEmailDomainInvitation

