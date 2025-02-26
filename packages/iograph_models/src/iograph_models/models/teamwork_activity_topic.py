from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamworkActivityTopic(BaseModel):
	source: Optional[TeamworkActivityTopicSource] = Field(default=None,alias="source",)
	value: Optional[str] = Field(default=None,alias="value",)
	webUrl: Optional[str] = Field(default=None,alias="webUrl",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .teamwork_activity_topic_source import TeamworkActivityTopicSource

