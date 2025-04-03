from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class DirectoryRoleAccessReviewPolicy(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.directoryRoleAccessReviewPolicy"] = Field(alias="@odata.type", default="#microsoft.graph.directoryRoleAccessReviewPolicy")
	settings: Optional[AccessReviewScheduleSettings] = Field(alias="settings", default=None,)

from .access_review_schedule_settings import AccessReviewScheduleSettings
