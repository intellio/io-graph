from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommunicationsIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="application",)
	device: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="device",)
	user: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationInstance: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="applicationInstance",)
	assertedIdentity: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="assertedIdentity",)
	azureCommunicationServicesUser: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="azureCommunicationServicesUser",)
	encrypted: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="encrypted",)
	endpointType: Optional[EndpointType] = Field(default=None,alias="endpointType",)
	guest: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="guest",)
	onPremises: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="onPremises",)
	phone: SerializeAsAny[Optional[Identity]] = Field(default=None,alias="phone",)

from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .identity import Identity
from .endpoint_type import EndpointType
from .identity import Identity
from .identity import Identity
from .identity import Identity

