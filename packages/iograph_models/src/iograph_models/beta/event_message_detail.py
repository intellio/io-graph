from __future__ import annotations
from typing import Optional
from pydantic import model_validator, ModelWrapValidatorHandler, ValidationError
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, SerializeAsAny


class EventMessageDetail(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

	@model_validator(mode="wrap")
	def convert_discriminator_class(cls, data: Any, handler: ModelWrapValidatorHandler[Self]) -> Self:
		try:
			# check with parent model to catch any errors
			parent_validated_model = handler(data)
			# check if the discriminator field is present
			if "@odata.type" not in data:
				return parent_validated_model
			# get the discriminator value
			mapping_key = data["@odata.type"]
			if mapping_key == "#microsoft.graph.callEndedEventMessageDetail":
				from .call_ended_event_message_detail import CallEndedEventMessageDetail
				return CallEndedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.callRecordingEventMessageDetail":
				from .call_recording_event_message_detail import CallRecordingEventMessageDetail
				return CallRecordingEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.callStartedEventMessageDetail":
				from .call_started_event_message_detail import CallStartedEventMessageDetail
				return CallStartedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.callTranscriptEventMessageDetail":
				from .call_transcript_event_message_detail import CallTranscriptEventMessageDetail
				return CallTranscriptEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelAddedEventMessageDetail":
				from .channel_added_event_message_detail import ChannelAddedEventMessageDetail
				return ChannelAddedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelDeletedEventMessageDetail":
				from .channel_deleted_event_message_detail import ChannelDeletedEventMessageDetail
				return ChannelDeletedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelDescriptionUpdatedEventMessageDetail":
				from .channel_description_updated_event_message_detail import ChannelDescriptionUpdatedEventMessageDetail
				return ChannelDescriptionUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelRenamedEventMessageDetail":
				from .channel_renamed_event_message_detail import ChannelRenamedEventMessageDetail
				return ChannelRenamedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelSetAsFavoriteByDefaultEventMessageDetail":
				from .channel_set_as_favorite_by_default_event_message_detail import ChannelSetAsFavoriteByDefaultEventMessageDetail
				return ChannelSetAsFavoriteByDefaultEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelSharingUpdatedEventMessageDetail":
				from .channel_sharing_updated_event_message_detail import ChannelSharingUpdatedEventMessageDetail
				return ChannelSharingUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.channelUnsetAsFavoriteByDefaultEventMessageDetail":
				from .channel_unset_as_favorite_by_default_event_message_detail import ChannelUnsetAsFavoriteByDefaultEventMessageDetail
				return ChannelUnsetAsFavoriteByDefaultEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.chatRenamedEventMessageDetail":
				from .chat_renamed_event_message_detail import ChatRenamedEventMessageDetail
				return ChatRenamedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.conversationMemberRoleUpdatedEventMessageDetail":
				from .conversation_member_role_updated_event_message_detail import ConversationMemberRoleUpdatedEventMessageDetail
				return ConversationMemberRoleUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.meetingPolicyUpdatedEventMessageDetail":
				from .meeting_policy_updated_event_message_detail import MeetingPolicyUpdatedEventMessageDetail
				return MeetingPolicyUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.membersAddedEventMessageDetail":
				from .members_added_event_message_detail import MembersAddedEventMessageDetail
				return MembersAddedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.membersDeletedEventMessageDetail":
				from .members_deleted_event_message_detail import MembersDeletedEventMessageDetail
				return MembersDeletedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.membersJoinedEventMessageDetail":
				from .members_joined_event_message_detail import MembersJoinedEventMessageDetail
				return MembersJoinedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.membersLeftEventMessageDetail":
				from .members_left_event_message_detail import MembersLeftEventMessageDetail
				return MembersLeftEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.messagePinnedEventMessageDetail":
				from .message_pinned_event_message_detail import MessagePinnedEventMessageDetail
				return MessagePinnedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.messageUnpinnedEventMessageDetail":
				from .message_unpinned_event_message_detail import MessageUnpinnedEventMessageDetail
				return MessageUnpinnedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.tabUpdatedEventMessageDetail":
				from .tab_updated_event_message_detail import TabUpdatedEventMessageDetail
				return TabUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamArchivedEventMessageDetail":
				from .team_archived_event_message_detail import TeamArchivedEventMessageDetail
				return TeamArchivedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamCreatedEventMessageDetail":
				from .team_created_event_message_detail import TeamCreatedEventMessageDetail
				return TeamCreatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamDescriptionUpdatedEventMessageDetail":
				from .team_description_updated_event_message_detail import TeamDescriptionUpdatedEventMessageDetail
				return TeamDescriptionUpdatedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamJoiningDisabledEventMessageDetail":
				from .team_joining_disabled_event_message_detail import TeamJoiningDisabledEventMessageDetail
				return TeamJoiningDisabledEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamJoiningEnabledEventMessageDetail":
				from .team_joining_enabled_event_message_detail import TeamJoiningEnabledEventMessageDetail
				return TeamJoiningEnabledEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamRenamedEventMessageDetail":
				from .team_renamed_event_message_detail import TeamRenamedEventMessageDetail
				return TeamRenamedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppInstalledEventMessageDetail":
				from .teams_app_installed_event_message_detail import TeamsAppInstalledEventMessageDetail
				return TeamsAppInstalledEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppRemovedEventMessageDetail":
				from .teams_app_removed_event_message_detail import TeamsAppRemovedEventMessageDetail
				return TeamsAppRemovedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamsAppUpgradedEventMessageDetail":
				from .teams_app_upgraded_event_message_detail import TeamsAppUpgradedEventMessageDetail
				return TeamsAppUpgradedEventMessageDetail.model_validate(data)
			if mapping_key == "#microsoft.graph.teamUnarchivedEventMessageDetail":
				from .team_unarchived_event_message_detail import TeamUnarchivedEventMessageDetail
				return TeamUnarchivedEventMessageDetail.model_validate(data)
			raise ValidationError(f"Invalid discriminator value: {mapping_key}")

		except Exception as e:
			raise e


