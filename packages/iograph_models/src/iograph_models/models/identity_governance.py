from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IdentityGovernance(BaseModel):
	accessReviews: Optional[AccessReviewSet] = Field(default=None,alias="accessReviews",)
	appConsent: Optional[AppConsentApprovalRoute] = Field(default=None,alias="appConsent",)
	entitlementManagement: Optional[EntitlementManagement] = Field(default=None,alias="entitlementManagement",)
	lifecycleWorkflows: Optional[IdentityGovernanceLifecycleWorkflowsContainer] = Field(default=None,alias="lifecycleWorkflows",)
	privilegedAccess: Optional[PrivilegedAccessRoot] = Field(default=None,alias="privilegedAccess",)
	termsOfUse: Optional[TermsOfUseContainer] = Field(default=None,alias="termsOfUse",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .access_review_set import AccessReviewSet
from .app_consent_approval_route import AppConsentApprovalRoute
from .entitlement_management import EntitlementManagement
from .identity_governance_lifecycle_workflows_container import IdentityGovernanceLifecycleWorkflowsContainer
from .privileged_access_root import PrivilegedAccessRoot
from .terms_of_use_container import TermsOfUseContainer

