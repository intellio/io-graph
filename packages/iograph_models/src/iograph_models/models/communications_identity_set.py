from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CommunicationsIdentitySet(BaseModel):
	application: Optional[Identity] = Field(default=None,alias="application",)
	device: Optional[Identity] = Field(default=None,alias="device",)
	user: Optional[Identity] = Field(default=None,alias="user",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	applicationInstance: Optional[Identity] = Field(default=None,alias="applicationInstance",)
	assertedIdentity: Optional[Identity] = Field(default=None,alias="assertedIdentity",)
	azureCommunicationServicesUser: Optional[Identity] = Field(default=None,alias="azureCommunicationServicesUser",)
	encrypted: Optional[Identity] = Field(default=None,alias="encrypted",)
	endpointType: Optional[EndpointType] = Field(default=None,alias="endpointType",)
	guest: Optional[Identity] = Field(default=None,alias="guest",)
	onPremises: Optional[Identity] = Field(default=None,alias="onPremises",)
	phone: Optional[Identity] = Field(default=None,alias="phone",)

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

