from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Send_activity_notification_to_recipientsPostRequest(BaseModel):
	topic: Optional[TeamworkActivityTopic] = Field(alias="topic",default=None,)
	activityType: Optional[str] = Field(alias="activityType",default=None,)
	chainId: Optional[int] = Field(alias="chainId",default=None,)
	previewText: Optional[ItemBody] = Field(alias="previewText",default=None,)
	teamsAppId: Optional[str] = Field(alias="teamsAppId",default=None,)
	templateParameters: Optional[list[KeyValuePair]] = Field(alias="templateParameters",default=None,)
	recipients: SerializeAsAny[Optional[list[TeamworkNotificationRecipient]]] = Field(alias="recipients",default=None,)

from .teamwork_activity_topic import TeamworkActivityTopic
from .item_body import ItemBody
from .key_value_pair import KeyValuePair
from .teamwork_notification_recipient import TeamworkNotificationRecipient

