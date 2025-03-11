from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CommunicationsIdentitySet(BaseModel):
	application: SerializeAsAny[Optional[Identity]] = Field(alias="application",default=None,)
	device: SerializeAsAny[Optional[Identity]] = Field(alias="device",default=None,)
	user: SerializeAsAny[Optional[Identity]] = Field(alias="user",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	applicationInstance: SerializeAsAny[Optional[Identity]] = Field(alias="applicationInstance",default=None,)
	assertedIdentity: SerializeAsAny[Optional[Identity]] = Field(alias="assertedIdentity",default=None,)
	azureCommunicationServicesUser: SerializeAsAny[Optional[Identity]] = Field(alias="azureCommunicationServicesUser",default=None,)
	encrypted: SerializeAsAny[Optional[Identity]] = Field(alias="encrypted",default=None,)
	endpointType: Optional[EndpointType | str] = Field(alias="endpointType",default=None,)
	guest: SerializeAsAny[Optional[Identity]] = Field(alias="guest",default=None,)
	onPremises: SerializeAsAny[Optional[Identity]] = Field(alias="onPremises",default=None,)
	phone: SerializeAsAny[Optional[Identity]] = Field(alias="phone",default=None,)

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

