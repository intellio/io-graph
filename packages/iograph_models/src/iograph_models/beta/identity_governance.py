from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernance(BaseModel):
	accessReviews: Optional[AccessReviewSet] = Field(alias="accessReviews",default=None,)
	appConsent: Optional[AppConsentApprovalRoute] = Field(alias="appConsent",default=None,)
	entitlementManagement: Optional[EntitlementManagement] = Field(alias="entitlementManagement",default=None,)
	lifecycleWorkflows: Optional[IdentityGovernanceLifecycleWorkflowsContainer] = Field(alias="lifecycleWorkflows",default=None,)
	permissionsAnalytics: Optional[PermissionsAnalyticsAggregation] = Field(alias="permissionsAnalytics",default=None,)
	permissionsManagement: Optional[PermissionsManagement] = Field(alias="permissionsManagement",default=None,)
	privilegedAccess: Optional[PrivilegedAccessRoot] = Field(alias="privilegedAccess",default=None,)
	roleManagementAlerts: Optional[RoleManagementAlert] = Field(alias="roleManagementAlerts",default=None,)
	termsOfUse: Optional[TermsOfUseContainer] = Field(alias="termsOfUse",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .access_review_set import AccessReviewSet
from .app_consent_approval_route import AppConsentApprovalRoute
from .entitlement_management import EntitlementManagement
from .identity_governance_lifecycle_workflows_container import IdentityGovernanceLifecycleWorkflowsContainer
from .permissions_analytics_aggregation import PermissionsAnalyticsAggregation
from .permissions_management import PermissionsManagement
from .privileged_access_root import PrivilegedAccessRoot
from .role_management_alert import RoleManagementAlert
from .terms_of_use_container import TermsOfUseContainer

