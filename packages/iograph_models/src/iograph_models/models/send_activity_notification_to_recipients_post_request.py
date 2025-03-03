from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Send_activity_notification_to_recipientsPostRequest(BaseModel):
	topic: Optional[TeamworkActivityTopic] = Field(default=None,alias="topic",)
	activityType: Optional[str] = Field(default=None,alias="activityType",)
	chainId: Optional[int] = Field(default=None,alias="chainId",)
	previewText: Optional[ItemBody] = Field(default=None,alias="previewText",)
	teamsAppId: Optional[str] = Field(default=None,alias="teamsAppId",)
	templateParameters: Optional[list[KeyValuePair]] = Field(default=None,alias="templateParameters",)
	recipients: Optional[list[TeamworkNotificationRecipient]] = Field(default=None,alias="recipients",)

from .teamwork_activity_topic import TeamworkActivityTopic
from .item_body import ItemBody
from .key_value_pair import KeyValuePair
from .teamwork_notification_recipient import TeamworkNotificationRecipient

