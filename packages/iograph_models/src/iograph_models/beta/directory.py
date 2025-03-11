from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Directory(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	administrativeUnits: Optional[list[AdministrativeUnit]] = Field(alias="administrativeUnits",default=None,)
	attributeSets: Optional[list[AttributeSet]] = Field(alias="attributeSets",default=None,)
	authenticationMethodDevices: SerializeAsAny[Optional[AuthenticationMethodDevice]] = Field(alias="authenticationMethodDevices",default=None,)
	certificateAuthorities: Optional[CertificateAuthorityPath] = Field(alias="certificateAuthorities",default=None,)
	customSecurityAttributeDefinitions: Optional[list[CustomSecurityAttributeDefinition]] = Field(alias="customSecurityAttributeDefinitions",default=None,)
	deletedItems: SerializeAsAny[Optional[list[DirectoryObject]]] = Field(alias="deletedItems",default=None,)
	deviceLocalCredentials: Optional[list[DeviceLocalCredentialInfo]] = Field(alias="deviceLocalCredentials",default=None,)
	externalUserProfiles: Optional[list[ExternalUserProfile]] = Field(alias="externalUserProfiles",default=None,)
	featureRolloutPolicies: Optional[list[FeatureRolloutPolicy]] = Field(alias="featureRolloutPolicies",default=None,)
	federationConfigurations: SerializeAsAny[Optional[list[IdentityProviderBase]]] = Field(alias="federationConfigurations",default=None,)
	impactedResources: Optional[list[ImpactedResource]] = Field(alias="impactedResources",default=None,)
	inboundSharedUserProfiles: Optional[list[InboundSharedUserProfile]] = Field(alias="inboundSharedUserProfiles",default=None,)
	onPremisesSynchronization: Optional[list[OnPremisesDirectorySynchronization]] = Field(alias="onPremisesSynchronization",default=None,)
	outboundSharedUserProfiles: Optional[list[OutboundSharedUserProfile]] = Field(alias="outboundSharedUserProfiles",default=None,)
	pendingExternalUserProfiles: Optional[list[PendingExternalUserProfile]] = Field(alias="pendingExternalUserProfiles",default=None,)
	publicKeyInfrastructure: Optional[PublicKeyInfrastructureRoot] = Field(alias="publicKeyInfrastructure",default=None,)
	recommendations: Optional[list[Recommendation]] = Field(alias="recommendations",default=None,)
	sharedEmailDomains: Optional[list[SharedEmailDomain]] = Field(alias="sharedEmailDomains",default=None,)
	subscriptions: Optional[list[CompanySubscription]] = Field(alias="subscriptions",default=None,)
	templates: Optional[Template] = Field(alias="templates",default=None,)

from .administrative_unit import AdministrativeUnit
from .attribute_set import AttributeSet
from .authentication_method_device import AuthenticationMethodDevice
from .certificate_authority_path import CertificateAuthorityPath
from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
from .directory_object import DirectoryObject
from .device_local_credential_info import DeviceLocalCredentialInfo
from .external_user_profile import ExternalUserProfile
from .feature_rollout_policy import FeatureRolloutPolicy
from .identity_provider_base import IdentityProviderBase
from .impacted_resource import ImpactedResource
from .inbound_shared_user_profile import InboundSharedUserProfile
from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
from .outbound_shared_user_profile import OutboundSharedUserProfile
from .pending_external_user_profile import PendingExternalUserProfile
from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
from .recommendation import Recommendation
from .shared_email_domain import SharedEmailDomain
from .company_subscription import CompanySubscription
from .template import Template

