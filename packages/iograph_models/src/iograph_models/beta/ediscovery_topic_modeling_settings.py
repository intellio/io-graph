from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EdiscoveryTopicModelingSettings(BaseModel):
	dynamicallyAdjustTopicCount: Optional[bool] = Field(alias="dynamicallyAdjustTopicCount",default=None,)
	ignoreNumbers: Optional[bool] = Field(alias="ignoreNumbers",default=None,)
	isEnabled: Optional[bool] = Field(alias="isEnabled",default=None,)
	topicCount: Optional[int] = Field(alias="topicCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


