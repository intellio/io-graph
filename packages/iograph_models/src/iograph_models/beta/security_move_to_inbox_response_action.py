from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityMoveToInboxResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.moveToInboxResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.moveToInboxResponseAction")
	identifier: Optional[SecurityEmailEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_email_entity_identifier import SecurityEmailEntityIdentifier
