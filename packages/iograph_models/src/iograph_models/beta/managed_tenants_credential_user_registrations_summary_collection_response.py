from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ManagedTenantsCredentialUserRegistrationsSummaryCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[ManagedTenantsCredentialUserRegistrationsSummary]] = Field(alias="value",default=None,)

from .managed_tenants_credential_user_registrations_summary import ManagedTenantsCredentialUserRegistrationsSummary

