from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Organization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	assignedPlans: list[AssignedPlan] = Field(alias="assignedPlans",)
	businessPhones: list[str] = Field(alias="businessPhones",)
	city: Optional[str] = Field(default=None,alias="city",)
	country: Optional[str] = Field(default=None,alias="country",)
	countryLetterCode: Optional[str] = Field(default=None,alias="countryLetterCode",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	defaultUsageLocation: Optional[str] = Field(default=None,alias="defaultUsageLocation",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	marketingNotificationEmails: list[str] = Field(alias="marketingNotificationEmails",)
	mobileDeviceManagementAuthority: Optional[MdmAuthority] = Field(default=None,alias="mobileDeviceManagementAuthority",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	partnerTenantType: Optional[PartnerTenantType] = Field(default=None,alias="partnerTenantType",)
	postalCode: Optional[str] = Field(default=None,alias="postalCode",)
	preferredLanguage: Optional[str] = Field(default=None,alias="preferredLanguage",)
	privacyProfile: Optional[PrivacyProfile] = Field(default=None,alias="privacyProfile",)
	provisionedPlans: list[ProvisionedPlan] = Field(alias="provisionedPlans",)
	securityComplianceNotificationMails: list[str] = Field(alias="securityComplianceNotificationMails",)
	securityComplianceNotificationPhones: list[str] = Field(alias="securityComplianceNotificationPhones",)
	state: Optional[str] = Field(default=None,alias="state",)
	street: Optional[str] = Field(default=None,alias="street",)
	technicalNotificationMails: list[str] = Field(alias="technicalNotificationMails",)
	tenantType: Optional[str] = Field(default=None,alias="tenantType",)
	verifiedDomains: list[VerifiedDomain] = Field(alias="verifiedDomains",)
	branding: Optional[OrganizationalBranding] = Field(default=None,alias="branding",)
	certificateBasedAuthConfiguration: list[CertificateBasedAuthConfiguration] = Field(alias="certificateBasedAuthConfiguration",)
	extensions: list[Extension] = Field(alias="extensions",)

from .assigned_plan import AssignedPlan
from .mdm_authority import MdmAuthority
from .partner_tenant_type import PartnerTenantType
from .privacy_profile import PrivacyProfile
from .provisioned_plan import ProvisionedPlan
from .verified_domain import VerifiedDomain
from .organizational_branding import OrganizationalBranding
from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
from .extension import Extension

