from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field


class PolicyBaseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[AppManagementPolicy, AuthorizationPolicy, ExternalIdentitiesPolicy, IdentitySecurityDefaultsEnforcementPolicy, PermissionGrantPolicy, ServicePrincipalCreationPolicy, ActivityBasedTimeoutPolicy, ClaimsMappingPolicy, HomeRealmDiscoveryPolicy, TokenIssuancePolicy, TokenLifetimePolicy, TenantAppManagementPolicy, CrossTenantAccessPolicy],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .app_management_policy import AppManagementPolicy
from .authorization_policy import AuthorizationPolicy
from .external_identities_policy import ExternalIdentitiesPolicy
from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
from .permission_grant_policy import PermissionGrantPolicy
from .service_principal_creation_policy import ServicePrincipalCreationPolicy
from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
from .claims_mapping_policy import ClaimsMappingPolicy
from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
from .token_issuance_policy import TokenIssuancePolicy
from .token_lifetime_policy import TokenLifetimePolicy
from .tenant_app_management_policy import TenantAppManagementPolicy
from .cross_tenant_access_policy import CrossTenantAccessPolicy
