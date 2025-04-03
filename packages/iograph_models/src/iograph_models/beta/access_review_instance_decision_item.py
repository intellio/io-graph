from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReviewInstanceDecisionItem(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewInstanceDecisionItem"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewInstanceDecisionItem")
	accessReviewId: Optional[str] = Field(alias="accessReviewId", default=None,)
	appliedBy: Optional[Union[AuditUserIdentity]] = Field(alias="appliedBy", default=None,discriminator="odata_type", )
	appliedDateTime: Optional[datetime] = Field(alias="appliedDateTime", default=None,)
	applyResult: Optional[str] = Field(alias="applyResult", default=None,)
	decision: Optional[str] = Field(alias="decision", default=None,)
	justification: Optional[str] = Field(alias="justification", default=None,)
	principal: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProgramResource, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, SourceProvisionedIdentity, TargetProvisionedIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, AuditUserIdentity, CallRecordsUserIdentity, SecuritySubmissionUserIdentity]] = Field(alias="principal", default=None,discriminator="odata_type", )
	principalLink: Optional[str] = Field(alias="principalLink", default=None,)
	principalResourceMembership: Optional[DecisionItemPrincipalResourceMembership] = Field(alias="principalResourceMembership", default=None,)
	recommendation: Optional[str] = Field(alias="recommendation", default=None,)
	resource: Optional[Union[AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource, AccessReviewInstanceDecisionItemAzureRoleResource, AccessReviewInstanceDecisionItemServicePrincipalResource]] = Field(alias="resource", default=None,discriminator="odata_type", )
	resourceLink: Optional[str] = Field(alias="resourceLink", default=None,)
	reviewedBy: Optional[Union[AuditUserIdentity]] = Field(alias="reviewedBy", default=None,discriminator="odata_type", )
	reviewedDateTime: Optional[datetime] = Field(alias="reviewedDateTime", default=None,)
	target: Optional[Union[AccessReviewInstanceDecisionItemServicePrincipalTarget, AccessReviewInstanceDecisionItemUserTarget]] = Field(alias="target", default=None,discriminator="odata_type", )
	insights: Optional[list[Annotated[Union[MembershipOutlierInsight, UserSignInInsight],Field(discriminator="odata_type")]]] = Field(alias="insights", default=None,)
	instance: Optional[AccessReviewInstance] = Field(alias="instance", default=None,)

from .audit_user_identity import AuditUserIdentity
from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
from .communications_application_identity import CommunicationsApplicationIdentity
from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
from .communications_encrypted_identity import CommunicationsEncryptedIdentity
from .communications_guest_identity import CommunicationsGuestIdentity
from .communications_phone_identity import CommunicationsPhoneIdentity
from .communications_user_identity import CommunicationsUserIdentity
from .email_identity import EmailIdentity
from .initiator import Initiator
from .program_resource import ProgramResource
from .provisioned_identity import ProvisionedIdentity
from .provisioning_service_principal import ProvisioningServicePrincipal
from .provisioning_system import ProvisioningSystem
from .service_principal_identity import ServicePrincipalIdentity
from .share_point_identity import SharePointIdentity
from .source_provisioned_identity import SourceProvisionedIdentity
from .target_provisioned_identity import TargetProvisionedIdentity
from .teamwork_application_identity import TeamworkApplicationIdentity
from .teamwork_conversation_identity import TeamworkConversationIdentity
from .teamwork_tag_identity import TeamworkTagIdentity
from .teamwork_user_identity import TeamworkUserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .security_submission_user_identity import SecuritySubmissionUserIdentity
from .decision_item_principal_resource_membership import DecisionItemPrincipalResourceMembership
from .access_review_instance_decision_item_access_package_assignment_policy_resource import AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
from .access_review_instance_decision_item_azure_role_resource import AccessReviewInstanceDecisionItemAzureRoleResource
from .access_review_instance_decision_item_service_principal_resource import AccessReviewInstanceDecisionItemServicePrincipalResource
from .access_review_instance_decision_item_service_principal_target import AccessReviewInstanceDecisionItemServicePrincipalTarget
from .access_review_instance_decision_item_user_target import AccessReviewInstanceDecisionItemUserTarget
from .membership_outlier_insight import MembershipOutlierInsight
from .user_sign_in_insight import UserSignInInsight
from .access_review_instance import AccessReviewInstance
