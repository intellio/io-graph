from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityStopAndQuarantineFileResponseAction(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	identifier: Optional[SecurityStopAndQuarantineFileEntityIdentifier | str] = Field(alias="identifier",default=None,)

from .security_stop_and_quarantine_file_entity_identifier import SecurityStopAndQuarantineFileEntityIdentifier

