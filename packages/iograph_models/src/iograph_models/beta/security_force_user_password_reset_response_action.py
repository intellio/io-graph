from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityForceUserPasswordResetResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityForceUserPasswordResetEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_force_user_password_reset_entity_identifier import SecurityForceUserPasswordResetEntityIdentifier

