from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityMarkUserAsCompromisedResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityMarkUserAsCompromisedEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_mark_user_as_compromised_entity_identifier import SecurityMarkUserAsCompromisedEntityIdentifier

