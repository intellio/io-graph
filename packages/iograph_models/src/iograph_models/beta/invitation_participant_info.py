from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class InvitationParticipantInfo(BaseModel):
	endpointType: Optional[EndpointType | str] = Field(alias="endpointType",default=None,)
	hidden: Optional[bool] = Field(alias="hidden",default=None,)
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="identity",default=None,)
	participantId: Optional[str] = Field(alias="participantId",default=None,)
	removeFromDefaultAudioRoutingGroup: Optional[bool] = Field(alias="removeFromDefaultAudioRoutingGroup",default=None,)
	replacesCallId: Optional[str] = Field(alias="replacesCallId",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .endpoint_type import EndpointType
from .identity_set import IdentitySet

