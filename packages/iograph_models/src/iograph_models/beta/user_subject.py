from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class UserSubject(BaseModel):
	odata_type: Literal["#microsoft.graph.userSubject"] = Field(alias="@odata.type", default="#microsoft.graph.userSubject")
	externalTenantId: Optional[str] = Field(alias="externalTenantId", default=None,)
	externalUserType: Optional[ConditionalAccessGuestOrExternalUserTypes | str] = Field(alias="externalUserType", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)

from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

