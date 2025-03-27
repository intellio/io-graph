from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityStopAndQuarantineFileResponseAction(BaseModel):
	odata_type: Literal["#microsoft.graph.security.stopAndQuarantineFileResponseAction"] = Field(alias="@odata.type", default="#microsoft.graph.security.stopAndQuarantineFileResponseAction")
	identifier: Optional[SecurityStopAndQuarantineFileEntityIdentifier | str] = Field(alias="identifier", default=None,)

from .security_stop_and_quarantine_file_entity_identifier import SecurityStopAndQuarantineFileEntityIdentifier

