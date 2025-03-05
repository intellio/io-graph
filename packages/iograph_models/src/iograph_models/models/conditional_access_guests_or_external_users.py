from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessGuestsOrExternalUsers(BaseModel):
	externalTenants: SerializeAsAny[Optional[ConditionalAccessExternalTenants]] = Field(default=None,alias="externalTenants",)
	guestOrExternalUserTypes: Optional[ConditionalAccessGuestOrExternalUserTypes] = Field(default=None,alias="guestOrExternalUserTypes",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .conditional_access_external_tenants import ConditionalAccessExternalTenants
from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

