from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Directory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	administrativeUnits: list[AdministrativeUnit] = Field(alias="administrativeUnits",)
	attributeSets: list[AttributeSet] = Field(alias="attributeSets",)
	customSecurityAttributeDefinitions: list[CustomSecurityAttributeDefinition] = Field(alias="customSecurityAttributeDefinitions",)
	deletedItems: list[DirectoryObject] = Field(alias="deletedItems",)
	deviceLocalCredentials: list[DeviceLocalCredentialInfo] = Field(alias="deviceLocalCredentials",)
	federationConfigurations: list[IdentityProviderBase] = Field(alias="federationConfigurations",)
	onPremisesSynchronization: list[OnPremisesDirectorySynchronization] = Field(alias="onPremisesSynchronization",)
	subscriptions: list[CompanySubscription] = Field(alias="subscriptions",)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
from .directory_object import DirectoryObject
from .device_local_credential_info import DeviceLocalCredentialInfo
from .identity_provider_base import IdentityProviderBase
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .company_subscription import CompanySubscription

