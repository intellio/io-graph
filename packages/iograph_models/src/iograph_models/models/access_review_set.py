from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AccessReviewSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	definitions: list[AccessReviewScheduleDefinition] = Field(alias="definitions",)
	historyDefinitions: list[AccessReviewHistoryDefinition] = Field(alias="historyDefinitions",)

from .access_review_schedule_definition import AccessReviewScheduleDefinition
from .access_review_history_definition import AccessReviewHistoryDefinition

