from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Organization(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	deletedDateTime: Optional[datetime] = Field(default=None,alias="deletedDateTime",)
	assignedPlans: Optional[list[AssignedPlan]] = Field(default=None,alias="assignedPlans",)
	businessPhones: Optional[list[str]] = Field(default=None,alias="businessPhones",)
	city: Optional[str] = Field(default=None,alias="city",)
	country: Optional[str] = Field(default=None,alias="country",)
	countryLetterCode: Optional[str] = Field(default=None,alias="countryLetterCode",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	defaultUsageLocation: Optional[str] = Field(default=None,alias="defaultUsageLocation",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	marketingNotificationEmails: Optional[list[str]] = Field(default=None,alias="marketingNotificationEmails",)
	mobileDeviceManagementAuthority: Optional[MdmAuthority] = Field(default=None,alias="mobileDeviceManagementAuthority",)
	onPremisesLastSyncDateTime: Optional[datetime] = Field(default=None,alias="onPremisesLastSyncDateTime",)
	onPremisesSyncEnabled: Optional[bool] = Field(default=None,alias="onPremisesSyncEnabled",)
	partnerTenantType: Optional[PartnerTenantType] = Field(default=None,alias="partnerTenantType",)
	postalCode: Optional[str] = Field(default=None,alias="postalCode",)
	preferredLanguage: Optional[str] = Field(default=None,alias="preferredLanguage",)
	privacyProfile: Optional[PrivacyProfile] = Field(default=None,alias="privacyProfile",)
	provisionedPlans: Optional[list[ProvisionedPlan]] = Field(default=None,alias="provisionedPlans",)
	securityComplianceNotificationMails: Optional[list[str]] = Field(default=None,alias="securityComplianceNotificationMails",)
	securityComplianceNotificationPhones: Optional[list[str]] = Field(default=None,alias="securityComplianceNotificationPhones",)
	state: Optional[str] = Field(default=None,alias="state",)
	street: Optional[str] = Field(default=None,alias="street",)
	technicalNotificationMails: Optional[list[str]] = Field(default=None,alias="technicalNotificationMails",)
	tenantType: Optional[str] = Field(default=None,alias="tenantType",)
	verifiedDomains: Optional[list[VerifiedDomain]] = Field(default=None,alias="verifiedDomains",)
	branding: Optional[OrganizationalBranding] = Field(default=None,alias="branding",)
	certificateBasedAuthConfiguration: Optional[list[CertificateBasedAuthConfiguration]] = Field(default=None,alias="certificateBasedAuthConfiguration",)
	extensions: Optional[list[Extension]] = Field(default=None,alias="extensions",)

from .assigned_plan import AssignedPlan
from .mdm_authority import MdmAuthority
from .partner_tenant_type import PartnerTenantType
from .privacy_profile import PrivacyProfile
from .provisioned_plan import ProvisionedPlan
from .verified_domain import VerifiedDomain
from .organizational_branding import OrganizationalBranding
from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
from .extension import Extension

