from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TeamworkActivityTopic(BaseModel):
	source: Optional[str | TeamworkActivityTopicSource] = Field(alias="source",default=None,)
	value: Optional[str] = Field(alias="value",default=None,)
	webUrl: Optional[str] = Field(alias="webUrl",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .teamwork_activity_topic_source import TeamworkActivityTopicSource

