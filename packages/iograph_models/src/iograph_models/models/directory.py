from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Directory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	administrativeUnits: Optional[list[AdministrativeUnit]] = Field(alias="administrativeUnits",default=None,)
	attributeSets: Optional[list[AttributeSet]] = Field(alias="attributeSets",default=None,)
	customSecurityAttributeDefinitions: Optional[list[CustomSecurityAttributeDefinition]] = Field(alias="customSecurityAttributeDefinitions",default=None,)
	deletedItems: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="deletedItems",default=None,)
	deviceLocalCredentials: Optional[list[DeviceLocalCredentialInfo]] = Field(alias="deviceLocalCredentials",default=None,)
	federationConfigurations: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(alias="federationConfigurations",default=None,)
	onPremisesSynchronization: Optional[list[OnPremisesDirectorySynchronization]] = Field(alias="onPremisesSynchronization",default=None,)
	subscriptions: Optional[list[CompanySubscription]] = Field(alias="subscriptions",default=None,)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
from .directory_object import DirectoryObject
from .device_local_credential_info import DeviceLocalCredentialInfo
from .identity_provider_base import IdentityProviderBase
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .company_subscription import CompanySubscription

