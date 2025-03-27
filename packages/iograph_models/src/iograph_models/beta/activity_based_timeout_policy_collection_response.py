from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ActivityBasedTimeoutPolicyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ActivityBasedTimeoutPolicy]] = Field(alias="value", default=None,)

from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy

