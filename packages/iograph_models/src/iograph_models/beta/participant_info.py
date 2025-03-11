from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ParticipantInfo(BaseModel):
	countryCode: Optional[str] = Field(alias="countryCode",default=None,)
	endpointType: Optional[EndpointType | str] = Field(alias="endpointType",default=None,)
	identity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="identity",default=None,)
	languageId: Optional[str] = Field(alias="languageId",default=None,)
	nonAnonymizedIdentity: SerializeAsAny[Optional[IdentitySet]] = Field(alias="nonAnonymizedIdentity",default=None,)
	participantId: Optional[str] = Field(alias="participantId",default=None,)
	platformId: Optional[str] = Field(alias="platformId",default=None,)
	region: Optional[str] = Field(alias="region",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .endpoint_type import EndpointType
from .identity_set import IdentitySet
from .identity_set import IdentitySet

