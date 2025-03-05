from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SharingInvitation(BaseModel):
	email: Optional[str] = Field(default=None,alias="email",)
	invitedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="invitedBy",)
	redeemedBy: Optional[str] = Field(default=None,alias="redeemedBy",)
	signInRequired: Optional[bool] = Field(default=None,alias="signInRequired",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet

