from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class OperationApprovalRequest(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.operationApprovalRequest"] = Field(alias="@odata.type",)
	approvalJustification: Optional[str] = Field(alias="approvalJustification", default=None,)
	approver: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="approver", default=None,discriminator="odata_type", )
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	requestDateTime: Optional[datetime] = Field(alias="requestDateTime", default=None,)
	requestJustification: Optional[str] = Field(alias="requestJustification", default=None,)
	requestor: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="requestor", default=None,discriminator="odata_type", )
	requiredOperationApprovalPolicyTypes: Optional[list[OperationApprovalPolicyType | str]] = Field(alias="requiredOperationApprovalPolicyTypes", default=None,)
	status: Optional[OperationApprovalRequestStatus | str] = Field(alias="status", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .operation_approval_policy_type import OperationApprovalPolicyType
from .operation_approval_request_status import OperationApprovalRequestStatus
