from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityForceUserPasswordResetResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.forceUserPasswordResetResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.forceUserPasswordResetResponseAction")
	identifier: Optional[SecurityForceUserPasswordResetEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_force_user_password_reset_entity_identifier import SecurityForceUserPasswordResetEntityIdentifier
