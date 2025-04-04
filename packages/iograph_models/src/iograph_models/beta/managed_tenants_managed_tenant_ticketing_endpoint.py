from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class ManagedTenantsManagedTenantTicketingEndpoint(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.managedTenants.managedTenantTicketingEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.managedTenants.managedTenantTicketingEndpoint")
	createdByUserId: Optional[str] = Field(alias="createdByUserId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	emailAddress: Optional[str] = Field(alias="emailAddress", default=None,)
	lastActionByUserId: Optional[str] = Field(alias="lastActionByUserId", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	phoneNumber: Optional[str] = Field(alias="phoneNumber", default=None,)

