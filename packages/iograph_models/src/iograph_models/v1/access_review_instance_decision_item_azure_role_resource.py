from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewInstanceDecisionItemAzureRoleResource(BaseModel):
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	id: Optional[str] = Field(alias="id", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource")
	scope: Optional[Union[AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource, AccessReviewInstanceDecisionItemAzureRoleResource, AccessReviewInstanceDecisionItemServicePrincipalResource]] = Field(alias="scope", default=None,discriminator="odata_type", )

from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource

