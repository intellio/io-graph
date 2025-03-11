from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDisableUserResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityDisableUserEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_disable_user_entity_identifier import SecurityDisableUserEntityIdentifier

