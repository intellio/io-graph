from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Directory(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	administrativeUnits: Optional[list[AdministrativeUnit]] = Field(default=None,alias="administrativeUnits",)
	attributeSets: Optional[list[AttributeSet]] = Field(default=None,alias="attributeSets",)
	customSecurityAttributeDefinitions: Optional[list[CustomSecurityAttributeDefinition]] = Field(default=None,alias="customSecurityAttributeDefinitions",)
	deletedItems: Optional[list[DirectoryObject]] = Field(default=None,alias="deletedItems",)
	deviceLocalCredentials: Optional[list[DeviceLocalCredentialInfo]] = Field(default=None,alias="deviceLocalCredentials",)
	federationConfigurations: Optional[list[IdentityProviderBase]] = Field(default=None,alias="federationConfigurations",)
	onPremisesSynchronization: Optional[list[OnPremisesDirectorySynchronization]] = Field(default=None,alias="onPremisesSynchronization",)
	subscriptions: Optional[list[CompanySubscription]] = Field(default=None,alias="subscriptions",)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
from .directory_object import DirectoryObject
from .device_local_credential_info import DeviceLocalCredentialInfo
from .identity_provider_base import IdentityProviderBase
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .company_subscription import CompanySubscription

