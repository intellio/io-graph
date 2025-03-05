from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessGuestsOrExternalUsers(BaseModel):
	externalTenants: SerializeAsAny[Optional[ConditionalAccessExternalTenants]] = Field(alias="externalTenants",default=None,)
	guestOrExternalUserTypes: Optional[ConditionalAccessGuestOrExternalUserTypes | str] = Field(alias="guestOrExternalUserTypes",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .conditional_access_external_tenants import ConditionalAccessExternalTenants
from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

