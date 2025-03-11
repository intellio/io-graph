from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingInvitation(BaseModel):
	email: Optional[str] = Field(alias="email",default=None,)
	invitedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="invitedBy",default=None,)
	redeemedBy: Optional[str] = Field(alias="redeemedBy",default=None,)
	signInRequired: Optional[bool] = Field(alias="signInRequired",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet

