from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SubjectRightsRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.subjectRightsRequest"] = Field(alias="@odata.type",)
	assignedTo: Optional[Union[AzureCommunicationServicesUserIdentity, CommunicationsApplicationIdentity, CommunicationsApplicationInstanceIdentity, CommunicationsEncryptedIdentity, CommunicationsGuestIdentity, CommunicationsPhoneIdentity, CommunicationsUserIdentity, EmailIdentity, Initiator, ProvisionedIdentity, ProvisioningServicePrincipal, ProvisioningSystem, ServicePrincipalIdentity, SharePointIdentity, TeamworkApplicationIdentity, TeamworkConversationIdentity, TeamworkTagIdentity, TeamworkUserIdentity, UserIdentity, CallRecordsUserIdentity]] = Field(alias="assignedTo", default=None,discriminator="odata_type", )
	closedDateTime: Optional[datetime] = Field(alias="closedDateTime", default=None,)
	contentQuery: Optional[str] = Field(alias="contentQuery", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	dataSubject: Optional[DataSubject] = Field(alias="dataSubject", default=None,)
	dataSubjectType: Optional[DataSubjectType | str] = Field(alias="dataSubjectType", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	externalId: Optional[str] = Field(alias="externalId", default=None,)
	history: Optional[list[SubjectRightsRequestHistory]] = Field(alias="history", default=None,)
	includeAllVersions: Optional[bool] = Field(alias="includeAllVersions", default=None,)
	includeAuthoredContent: Optional[bool] = Field(alias="includeAuthoredContent", default=None,)
	insight: Optional[SubjectRightsRequestDetail] = Field(alias="insight", default=None,)
	internalDueDateTime: Optional[datetime] = Field(alias="internalDueDateTime", default=None,)
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	mailboxLocations: Optional[Union[SubjectRightsRequestAllMailboxLocation, SubjectRightsRequestEnumeratedMailboxLocation]] = Field(alias="mailboxLocations", default=None,discriminator="odata_type", )
	pauseAfterEstimate: Optional[bool] = Field(alias="pauseAfterEstimate", default=None,)
	regulations: Optional[list[str]] = Field(alias="regulations", default=None,)
	siteLocations: Optional[Union[SubjectRightsRequestAllSiteLocation, SubjectRightsRequestEnumeratedSiteLocation]] = Field(alias="siteLocations", default=None,discriminator="odata_type", )
	stages: Optional[list[SubjectRightsRequestStageDetail]] = Field(alias="stages", default=None,)
	status: Optional[SubjectRightsRequestStatus | str] = Field(alias="status", default=None,)
	type: Optional[SubjectRightsRequestType | str] = Field(alias="type", default=None,)
	approvers: Optional[list[User]] = Field(alias="approvers", default=None,)
	collaborators: Optional[list[User]] = Field(alias="collaborators", default=None,)
	notes: Optional[list[AuthoredNote]] = Field(alias="notes", default=None,)
	team: Optional[Team] = Field(alias="team", default=None,)

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
from .user_identity import UserIdentity
from .call_records_user_identity import CallRecordsUserIdentity
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .data_subject import DataSubject
from .data_subject_type import DataSubjectType
from .subject_rights_request_history import SubjectRightsRequestHistory
from .subject_rights_request_detail import SubjectRightsRequestDetail
from .subject_rights_request_all_mailbox_location import SubjectRightsRequestAllMailboxLocation
from .subject_rights_request_enumerated_mailbox_location import SubjectRightsRequestEnumeratedMailboxLocation
from .subject_rights_request_all_site_location import SubjectRightsRequestAllSiteLocation
from .subject_rights_request_enumerated_site_location import SubjectRightsRequestEnumeratedSiteLocation
from .subject_rights_request_stage_detail import SubjectRightsRequestStageDetail
from .subject_rights_request_status import SubjectRightsRequestStatus
from .subject_rights_request_type import SubjectRightsRequestType
from .user import User
from .authored_note import AuthoredNote
from .team import Team
