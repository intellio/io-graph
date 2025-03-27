from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMarkUserAsCompromisedResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.markUserAsCompromisedResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.markUserAsCompromisedResponseAction")
	identifier: Optional[SecurityMarkUserAsCompromisedEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_mark_user_as_compromised_entity_identifier import SecurityMarkUserAsCompromisedEntityIdentifier

