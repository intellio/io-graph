from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class Organization(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.organization"] = Field(alias="@odata.type", default="#microsoft.graph.organization")
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	assignedPlans: Optional[list[AssignedPlan]] = Field(alias="assignedPlans", default=None,)
	businessPhones: Optional[list[str]] = Field(alias="businessPhones", default=None,)
	city: Optional[str] = Field(alias="city", default=None,)
	country: Optional[str] = Field(alias="country", default=None,)
	countryLetterCode: Optional[str] = Field(alias="countryLetterCode", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	defaultUsageLocation: Optional[str] = Field(alias="defaultUsageLocation", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	marketingNotificationEmails: Optional[list[str]] = Field(alias="marketingNotificationEmails", default=None,)
	mobileDeviceManagementAuthority: Optional[MdmAuthority | str] = Field(alias="mobileDeviceManagementAuthority", default=None,)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(alias="onPremisesLastSyncDateTime", default=None,)
	onPremisesSyncEnabled: Optional[bool] = Field(alias="onPremisesSyncEnabled", default=None,)
	partnerTenantType: Optional[PartnerTenantType | str] = Field(alias="partnerTenantType", default=None,)
	postalCode: Optional[str] = Field(alias="postalCode", default=None,)
	preferredLanguage: Optional[str] = Field(alias="preferredLanguage", default=None,)
	privacyProfile: Optional[PrivacyProfile] = Field(alias="privacyProfile", default=None,)
	provisionedPlans: Optional[list[ProvisionedPlan]] = Field(alias="provisionedPlans", default=None,)
	securityComplianceNotificationMails: Optional[list[str]] = Field(alias="securityComplianceNotificationMails", default=None,)
	securityComplianceNotificationPhones: Optional[list[str]] = Field(alias="securityComplianceNotificationPhones", default=None,)
	state: Optional[str] = Field(alias="state", default=None,)
	street: Optional[str] = Field(alias="street", default=None,)
	technicalNotificationMails: Optional[list[str]] = Field(alias="technicalNotificationMails", default=None,)
	tenantType: Optional[str] = Field(alias="tenantType", default=None,)
	verifiedDomains: Optional[list[VerifiedDomain]] = Field(alias="verifiedDomains", default=None,)
	branding: Optional[OrganizationalBranding] = Field(alias="branding", default=None,)
	certificateBasedAuthConfiguration: Optional[list[CertificateBasedAuthConfiguration]] = Field(alias="certificateBasedAuthConfiguration", default=None,)
	extensions: Optional[list[Annotated[Union[OpenTypeExtension]],Field(discriminator="odata_type")]]] = Field(alias="extensions", default=None,)

from .assigned_plan import AssignedPlan
from .mdm_authority import MdmAuthority
from .partner_tenant_type import PartnerTenantType
from .privacy_profile import PrivacyProfile
from .provisioned_plan import ProvisionedPlan
from .verified_domain import VerifiedDomain
from .organizational_branding import OrganizationalBranding
from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
from .open_type_extension import OpenTypeExtension

