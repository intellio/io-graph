from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IncomingContext(BaseModel):
	observedParticipantId: Optional[str] = Field(default=None,alias="observedParticipantId",)
	onBehalfOf: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="onBehalfOf",)
	sourceParticipantId: Optional[str] = Field(default=None,alias="sourceParticipantId",)
	transferor: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="transferor",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

