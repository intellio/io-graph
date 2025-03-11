from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IncomingContext(BaseModel):
	observedParticipantId: Optional[str] = Field(alias="observedParticipantId",default=None,)
	onBehalfOf: SerializeAsAny[Optional[IdentitySet]] = Field(alias="onBehalfOf",default=None,)
	sourceParticipantId: Optional[str] = Field(alias="sourceParticipantId",default=None,)
	transferor: SerializeAsAny[Optional[IdentitySet]] = Field(alias="transferor",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .identity_set import IdentitySet
from .identity_set import IdentitySet

