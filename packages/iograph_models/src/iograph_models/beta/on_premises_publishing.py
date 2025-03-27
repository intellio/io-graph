from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesPublishing(BaseModel):
	alternateUrl: Optional[str] = Field(alias="alternateUrl", default=None,)
	applicationServerTimeout: Optional[str] = Field(alias="applicationServerTimeout", default=None,)
	applicationType: Optional[str] = Field(alias="applicationType", default=None,)
	externalAuthenticationType: Optional[ExternalAuthenticationType | str] = Field(alias="externalAuthenticationType", default=None,)
	externalUrl: Optional[str] = Field(alias="externalUrl", default=None,)
	internalUrl: Optional[str] = Field(alias="internalUrl", default=None,)
	isAccessibleViaZTNAClient: Optional[bool] = Field(alias="isAccessibleViaZTNAClient", default=None,)
	isBackendCertificateValidationEnabled: Optional[bool] = Field(alias="isBackendCertificateValidationEnabled", default=None,)
	isDnsResolutionEnabled: Optional[bool] = Field(alias="isDnsResolutionEnabled", default=None,)
	isHttpOnlyCookieEnabled: Optional[bool] = Field(alias="isHttpOnlyCookieEnabled", default=None,)
	isOnPremPublishingEnabled: Optional[bool] = Field(alias="isOnPremPublishingEnabled", default=None,)
	isPersistentCookieEnabled: Optional[bool] = Field(alias="isPersistentCookieEnabled", default=None,)
	isSecureCookieEnabled: Optional[bool] = Field(alias="isSecureCookieEnabled", default=None,)
	isStateSessionEnabled: Optional[bool] = Field(alias="isStateSessionEnabled", default=None,)
	isTranslateHostHeaderEnabled: Optional[bool] = Field(alias="isTranslateHostHeaderEnabled", default=None,)
	isTranslateLinksInBodyEnabled: Optional[bool] = Field(alias="isTranslateLinksInBodyEnabled", default=None,)
	onPremisesApplicationSegments: Optional[list[OnPremisesApplicationSegment]] = Field(alias="onPremisesApplicationSegments", default=None,)
	segmentsConfiguration: Optional[Union[IpSegmentConfiguration, WebSegmentConfiguration]] = Field(alias="segmentsConfiguration", default=None,discriminator="odata_type", )
	singleSignOnSettings: Optional[OnPremisesPublishingSingleSignOn] = Field(alias="singleSignOnSettings", default=None,)
	useAlternateUrlForTranslationAndRedirect: Optional[bool] = Field(alias="useAlternateUrlForTranslationAndRedirect", default=None,)
	verifiedCustomDomainCertificatesMetadata: Optional[VerifiedCustomDomainCertificatesMetadata] = Field(alias="verifiedCustomDomainCertificatesMetadata", default=None,)
	verifiedCustomDomainKeyCredential: Optional[KeyCredential] = Field(alias="verifiedCustomDomainKeyCredential", default=None,)
	verifiedCustomDomainPasswordCredential: Optional[PasswordCredential] = Field(alias="verifiedCustomDomainPasswordCredential", default=None,)
	wafAllowedHeaders: Optional[WafAllowedHeadersDictionary] = Field(alias="wafAllowedHeaders", default=None,)
	wafIpRanges: Optional[list[Annotated[Union[IPv4CidrRange, IPv4Range, IPv6CidrRange, IPv6Range]],Field(discriminator="odata_type")]]] = Field(alias="wafIpRanges", default=None,)
	wafProvider: Optional[str] = Field(alias="wafProvider", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .external_authentication_type import ExternalAuthenticationType
from .on_premises_application_segment import OnPremisesApplicationSegment
from .ip_segment_configuration import IpSegmentConfiguration
from .web_segment_configuration import WebSegmentConfiguration
from .on_premises_publishing_single_sign_on import OnPremisesPublishingSingleSignOn
from .verified_custom_domain_certificates_metadata import VerifiedCustomDomainCertificatesMetadata
from .key_credential import KeyCredential
from .password_credential import PasswordCredential
from .waf_allowed_headers_dictionary import WafAllowedHeadersDictionary
from .i_pv4_cidr_range import IPv4CidrRange
from .i_pv4_range import IPv4Range
from .i_pv6_cidr_range import IPv6CidrRange
from .i_pv6_range import IPv6Range

