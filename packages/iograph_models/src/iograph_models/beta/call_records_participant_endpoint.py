from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field


class CallRecordsParticipantEndpoint(BaseModel):
	userAgent: Optional[Union[CallRecordsClientUserAgent, CallRecordsServiceUserAgent]] = Field(alias="userAgent", default=None,discriminator="odata_type", )
	odata_type: Literal["#microsoft.graph.callRecords.participantEndpoint"] = Field(alias="@odata.type", default="#microsoft.graph.callRecords.participantEndpoint")
	associatedIdentity: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProgramResource, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, SourceProvisionedIdentity, TargetProvisionedIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, AuditUserIdentity, CallRecordsUserIdentity, SecuritySubmissionUserIdentity]] = Field(alias="associatedIdentity", default=None,discriminator="odata_type", )
	cpuCoresCount: Optional[int] = Field(alias="cpuCoresCount", default=None,)
	cpuName: Optional[str] = Field(alias="cpuName", default=None,)
	cpuProcessorSpeedInMhz: Optional[int] = Field(alias="cpuProcessorSpeedInMhz", default=None,)
	feedback: Optional[CallRecordsUserFeedback] = Field(alias="feedback", default=None,)
	identity: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="identity", default=None,discriminator="odata_type", )
	name: Optional[str] = Field(alias="name", default=None,)

from .call_records_client_user_agent import CallRecordsClientUserAgent
from .call_records_service_user_agent import CallRecordsServiceUserAgent
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
from .audit_user_identity import AuditUserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .security_submission_user_identity import SecuritySubmissionUserIdentity
from .call_records_user_feedback import CallRecordsUserFeedback
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
