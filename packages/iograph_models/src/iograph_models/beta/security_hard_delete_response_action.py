from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class SecurityHardDeleteResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.hardDeleteResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.hardDeleteResponseAction")
	identifier: Optional[SecurityEmailEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_email_entity_identifier import SecurityEmailEntityIdentifier
