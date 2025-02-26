from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ParticipantInfo(BaseModel):
	countryCode: Optional[str] = Field(default=None,alias="countryCode",)
	endpointType: Optional[EndpointType] = Field(default=None,alias="endpointType",)
	identity: Optional[IdentitySet] = Field(default=None,alias="identity",)
	languageId: Optional[str] = Field(default=None,alias="languageId",)
	participantId: Optional[str] = Field(default=None,alias="participantId",)
	region: Optional[str] = Field(default=None,alias="region",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .endpoint_type import EndpointType
from .identity_set import IdentitySet

