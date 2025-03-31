from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class DocumentSetVersion(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.documentSetVersion"] = Field(alias="@odata.type", default="#microsoft.graph.documentSetVersion")
	lastModifiedBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="lastModifiedBy", default=None,discriminator="odata_type", )
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	publication: Optional[PublicationFacet] = Field(alias="publication", default=None,)
	fields: Optional[FieldValueSet] = Field(alias="fields", default=None,)
	comment: Optional[str] = Field(alias="comment", default=None,)
	createdBy: Optional[Union[ChatMessageFromIdentitySet, ChatMessageMentionedIdentitySet, ChatMessageReactionIdentitySet, CommunicationsIdentitySet, SharePointIdentitySet]] = Field(alias="createdBy", default=None,discriminator="odata_type", )
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	items: Optional[list[DocumentSetVersionItem]] = Field(alias="items", default=None,)
	shouldCaptureMinorVersion: Optional[bool] = Field(alias="shouldCaptureMinorVersion", default=None,)

from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_mentioned_identity_set import ChatMessageMentionedIdentitySet
from .chat_message_reaction_identity_set import ChatMessageReactionIdentitySet
from .communications_identity_set import CommunicationsIdentitySet
from .share_point_identity_set import SharePointIdentitySet
from .publication_facet import PublicationFacet
from .field_value_set import FieldValueSet
from .document_set_version_item import DocumentSetVersionItem
