from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityTopicModelingSettings(BaseModel):
	dynamicallyAdjustTopicCount: Optional[bool] = Field(default=None,alias="dynamicallyAdjustTopicCount",)
	ignoreNumbers: Optional[bool] = Field(default=None,alias="ignoreNumbers",)
	isEnabled: Optional[bool] = Field(default=None,alias="isEnabled",)
	topicCount: Optional[int] = Field(default=None,alias="topicCount",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


