from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WorkforceIntegration(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.workforceIntegration"] = Field(alias="@odata.type", default="#microsoft.graph.workforceIntegration")
	createdBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastModifiedBy: Optional[Union[AiInteractionMentionedIdentitySet, ApprovalIdentitySet, ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	apiVersion: Optional[int] = Field(alias="apiVersion", default=None,)
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	eligibilityFilteringEnabledEntities: Optional[EligibilityFilteringEnabledEntities | str] = Field(alias="eligibilityFilteringEnabledEntities", default=None,)
	encryption: Optional[WorkforceIntegrationEncryption] = Field(alias="encryption", default=None,)
	isActive: Optional[bool] = Field(alias="isActive", default=None,)
	supportedEntities: Optional[WorkforceIntegrationSupportedEntities | str] = Field(alias="supportedEntities", default=None,)
	supports: Optional[WorkforceIntegrationSupportedEntities | str] = Field(alias="supports", default=None,)
	url: Optional[str] = Field(alias="url", default=None,)

from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet
from .approval_identity_set import ApprovalIdentitySet
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
from .workforce_integration_encryption import WorkforceIntegrationEncryption
from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities
from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

