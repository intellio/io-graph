from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class AccessReview(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReview"] = Field(alias="@odata.type",)
	businessFlowTemplateId: Optional[str] = Field(alias="businessFlowTemplateId", default=None,)
	createdBy: Optional[Union[AuditUserIdentity]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	endDateTime: Optional[datetime] = Field(alias="endDateTime", default=None,)
	reviewedEntity: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProgramResource, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, SourceProvisionedIdentity, TargetProvisionedIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, AuditUserIdentity, CallRecordsUserIdentity, SecuritySubmissionUserIdentity]] = Field(alias="reviewedEntity", default=None,discriminator="odata_type", )
	reviewerType: Optional[str] = Field(alias="reviewerType", default=None,)
	settings: Optional[Union[BusinessFlowSettings]] = Field(alias="settings", default=None,discriminator="odata_type", )
	startDateTime: Optional[datetime] = Field(alias="startDateTime", default=None,)
	status: Optional[str] = Field(alias="status", default=None,)
	decisions: Optional[list[AccessReviewDecision]] = Field(alias="decisions", default=None,)
	instances: Optional[list[AccessReview]] = Field(alias="instances", default=None,)
	myDecisions: Optional[list[AccessReviewDecision]] = Field(alias="myDecisions", default=None,)
	reviewers: Optional[list[AccessReviewReviewer]] = Field(alias="reviewers", default=None,)

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
from .business_flow_settings import BusinessFlowSettings
from .access_review_decision import AccessReviewDecision
from .access_review_reviewer import AccessReviewReviewer
