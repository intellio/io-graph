from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserTrainingStatusInfoCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserTrainingStatusInfo]] = Field(alias="value", default=None,)

from .user_training_status_info import UserTrainingStatusInfo
