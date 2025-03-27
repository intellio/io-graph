from __future__ import annotations
from typing import Optional
from typing import Union
from pydantic import BaseModel, Field, SerializeAsAny


class ConditionalAccessGuestsOrExternalUsers(BaseModel):
	externalTenants: Optional[Union[ConditionalAccessAllExternalTenants, ConditionalAccessEnumeratedExternalTenants]] = Field(alias="externalTenants", default=None,discriminator="odata_type", )
	guestOrExternalUserTypes: Optional[ConditionalAccessGuestOrExternalUserTypes | str] = Field(alias="guestOrExternalUserTypes", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants
from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants
from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

