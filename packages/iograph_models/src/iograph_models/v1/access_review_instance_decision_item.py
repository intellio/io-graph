from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItem"] = Field(alias="@odata.type",)
	accessReviewId: Optional[str] = Field(alias="accessReviewId", default=None,)
	appliedBy: Optional[UserIdentity] = Field(alias="appliedBy", default=None,)
	appliedDateTime: Optional[datetime] = Field(alias="appliedDateTime", default=None,)
	applyResult: Optional[str] = Field(alias="applyResult", default=None,)
	decision: Optional[str] = Field(alias="decision", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	principal: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, UserIdentity, CallRecordsUserIdentity]] = Field(alias="principal", default=None,discriminator="odata_type", )
	principalLink: Optional[str] = Field(alias="principalLink", default=None,)
	recommendation: Optional[str] = Field(alias="recommendation", default=None,)
	resource: Optional[Union[AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource, AccessReviewInstanceDecisionItemAzureRoleResource, AccessReviewInstanceDecisionItemServicePrincipalResource]] = Field(alias="resource", default=None,discriminator="odata_type", )
	resourceLink: Optional[str] = Field(alias="resourceLink", default=None,)
	reviewedBy: Optional[UserIdentity] = Field(alias="reviewedBy", default=None,)
	reviewedDateTime: Optional[datetime] = Field(alias="reviewedDateTime", default=None,)
	insights: Optional[list[Annotated[Union[MembershipOutlierInsight, UserSignInInsight],Field(discriminator="odata_type")]]] = Field(alias="insights", default=None,)

from .user_identity import UserIdentity
from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
from .communications_application_identity import CommunicationsApplicationIdentity
from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
from .communications_encrypted_identity import CommunicationsEncryptedIdentity
from .communications_guest_identity import CommunicationsGuestIdentity
from .communications_phone_identity import CommunicationsPhoneIdentity
from .communications_user_identity import CommunicationsUserIdentity
from .email_identity import EmailIdentity
from .initiator import Initiator
from .provisioned_identity import ProvisionedIdentity
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioning_system import ProvisioningSystem
from .service_principal_identity import ServicePrincipalIdentity
from .share_point_identity import SharePointIdentity
from .teamwork_application_identity import TeamworkApplicationIdentity
from .teamwork_conversation_identity import TeamworkConversationIdentity
from .teamwork_tag_identity import TeamworkTagIdentity
from .teamwork_user_identity import TeamworkUserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource
from .membership_outlier_insight import MembershipOutlierInsight
from .user_sign_in_insight import UserSignInInsight
