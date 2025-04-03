from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class SecurityEdiscoverySearchExportOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.security.ediscoverySearchExportOperation"] = Field(alias="@odata.type", default="#microsoft.graph.security.ediscoverySearchExportOperation")
	action: Optional[SecurityCaseAction | str] = Field(alias="action", default=None,)
	completedDateTime: Optional[datetime] = Field(alias="completedDateTime", default=None,)
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	percentProgress: Optional[int] = Field(alias="percentProgress", default=None,)
	resultInfo: Optional[ResultInfo] = Field(alias="resultInfo", default=None,)
	status: Optional[SecurityCaseOperationStatus | str] = Field(alias="status", default=None,)
	additionalOptions: Optional[SecurityAdditionalOptions | str] = Field(alias="additionalOptions", default=None,)
	cloudAttachmentVersion: Optional[SecurityCloudAttachmentVersion | str] = Field(alias="cloudAttachmentVersion", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	documentVersion: Optional[SecurityDocumentVersion | str] = Field(alias="documentVersion", default=None,)
	exportCriteria: Optional[SecurityExportCriteria | str] = Field(alias="exportCriteria", default=None,)
	exportFileMetadata: Optional[list[SecurityExportFileMetadata]] = Field(alias="exportFileMetadata", default=None,)
	exportFormat: Optional[SecurityExportFormat | str] = Field(alias="exportFormat", default=None,)
	exportLocation: Optional[SecurityExportLocation | str] = Field(alias="exportLocation", default=None,)
	exportSingleItems: Optional[bool] = Field(alias="exportSingleItems", default=None,)
	search: Optional[SecurityEdiscoverySearch] = Field(alias="search", default=None,)

from .security_case_action import SecurityCaseAction
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .result_info import ResultInfo
from .security_case_operation_status import SecurityCaseOperationStatus
from .security_additional_options import SecurityAdditionalOptions
from .security_cloud_attachment_version import SecurityCloudAttachmentVersion
from .security_document_version import SecurityDocumentVersion
from .security_export_criteria import SecurityExportCriteria
from .security_export_file_metadata import SecurityExportFileMetadata
from .security_export_format import SecurityExportFormat
from .security_export_location import SecurityExportLocation
from .security_ediscovery_search import SecurityEdiscoverySearch
