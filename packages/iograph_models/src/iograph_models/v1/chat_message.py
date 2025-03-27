from __future__ import annotations
from typing import Optional
from typing import Union
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ChatMessage(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	attachments: Optional[list[ChatMessageAttachment]] = Field(alias="attachments", default=None,)
	body: Optional[ItemBody] = Field(alias="body", default=None,)
	channelIdentity: Optional[ChannelIdentity] = Field(alias="channelIdentity", default=None,)
	chatId: Optional[str] = Field(alias="chatId", default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	deletedDateTime: Optional[datetime] = Field(alias="deletedDateTime", default=None,)
	etag: Optional[str] = Field(alias="etag", default=None,)
	eventDetail: Optional[Union[CallEndedEventMessageDetail, CallRecordingEventMessageDetail, CallStartedEventMessageDetail, CallTranscriptEventMessageDetail, ChannelAddedEventMessageDetail, ChannelDeletedEventMessageDetail, ChannelDescriptionUpdatedEventMessageDetail, ChannelRenamedEventMessageDetail, ChannelSetAsFavoriteByDefaultEventMessageDetail, ChannelUnsetAsFavoriteByDefaultEventMessageDetail, ChatRenamedEventMessageDetail, ConversationMemberRoleUpdatedEventMessageDetail, MeetingPolicyUpdatedEventMessageDetail, MembersAddedEventMessageDetail, MembersDeletedEventMessageDetail, MembersJoinedEventMessageDetail, MembersLeftEventMessageDetail, MessagePinnedEventMessageDetail, MessageUnpinnedEventMessageDetail, TabUpdatedEventMessageDetail, TeamArchivedEventMessageDetail, TeamCreatedEventMessageDetail, TeamDescriptionUpdatedEventMessageDetail, TeamJoiningDisabledEventMessageDetail, TeamJoiningEnabledEventMessageDetail, TeamRenamedEventMessageDetail, TeamsAppInstalledEventMessageDetail, TeamsAppRemovedEventMessageDetail, TeamsAppUpgradedEventMessageDetail, TeamUnarchivedEventMessageDetail]] = Field(alias="eventDetail", default=None,discriminator="odata_type", )
	from_: Optional[ChatMessageFromIdentitySet] = Field(alias="from", default=None,)
	importance: Optional[ChatMessageImportance | str] = Field(alias="importance", default=None,)
	lastEditedDateTime: Optional[datetime] = Field(alias="lastEditedDateTime", default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime", default=None,)
	locale: Optional[str] = Field(alias="locale", default=None,)
	mentions: Optional[list[ChatMessageMention]] = Field(alias="mentions", default=None,)
	messageHistory: Optional[list[ChatMessageHistoryItem]] = Field(alias="messageHistory", default=None,)
	messageType: Optional[ChatMessageType | str] = Field(alias="messageType", default=None,)
	policyViolation: Optional[ChatMessagePolicyViolation] = Field(alias="policyViolation", default=None,)
	reactions: Optional[list[ChatMessageReaction]] = Field(alias="reactions", default=None,)
	replyToId: Optional[str] = Field(alias="replyToId", default=None,)
	subject: Optional[str] = Field(alias="subject", default=None,)
	summary: Optional[str] = Field(alias="summary", default=None,)
	webUrl: Optional[str] = Field(alias="webUrl", default=None,)
	hostedContents: Optional[list[ChatMessageHostedContent]] = Field(alias="hostedContents", default=None,)
	replies: Optional[list[ChatMessage]] = Field(alias="replies", default=None,)

from .chat_message_attachment import ChatMessageAttachment
from .item_body import ItemBody
from .channel_identity import ChannelIdentity
from .call_ended_event_message_detail import CallEndedEventMessageDetail
from .call_recording_event_message_detail import CallRecordingEventMessageDetail
from .call_started_event_message_detail import CallStartedEventMessageDetail
from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail
from .channel_added_event_message_detail import ChannelAddedEventMessageDetail
from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail
from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail
from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail
from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail
from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail
from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail
from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail
from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail
from .members_added_event_message_detail import MembersAddedEventMessageDetail
from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail
from .members_joined_event_message_detail import MembersJoinedEventMessageDetail
from .members_left_event_message_detail import MembersLeftEventMessageDetail
from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail
from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail
from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail
from .team_archived_event_message_detail import TeamArchivedEventMessageDetail
from .team_created_event_message_detail import TeamCreatedEventMessageDetail
from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail
from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail
from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail
from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail
from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail
from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail
from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail
from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail
from .chat_message_from_identity_set import ChatMessageFromIdentitySet
from .chat_message_importance import ChatMessageImportance
from .chat_message_mention import ChatMessageMention
from .chat_message_history_item import ChatMessageHistoryItem
from .chat_message_type import ChatMessageType
from .chat_message_policy_violation import ChatMessagePolicyViolation
from .chat_message_reaction import ChatMessageReaction
from .chat_message_hosted_content import ChatMessageHostedContent

