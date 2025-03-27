from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityDisableUserResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.disableUserResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.disableUserResponseAction")
	identifier: Optional[SecurityDisableUserEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_disable_user_entity_identifier import SecurityDisableUserEntityIdentifier

