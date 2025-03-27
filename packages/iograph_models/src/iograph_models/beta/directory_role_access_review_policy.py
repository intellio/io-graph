from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DirectoryRoleAccessReviewPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	settings: Optional[AccessReviewScheduleSettings] = Field(alias="settings", default=None,)

from .access_review_schedule_settings import AccessReviewScheduleSettings

