from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AccessReviewSet(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	definitions: Optional[list[AccessReviewScheduleDefinition]] = Field(default=None,alias="definitions",)
	historyDefinitions: Optional[list[AccessReviewHistoryDefinition]] = Field(default=None,alias="historyDefinitions",)

from .access_review_schedule_definition import AccessReviewScheduleDefinition
from .access_review_history_definition import AccessReviewHistoryDefinition

