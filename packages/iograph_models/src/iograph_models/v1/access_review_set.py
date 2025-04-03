from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class AccessReviewSet(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.accessReviewSet"] = Field(alias="@odata.type", default="#microsoft.graph.accessReviewSet")
	definitions: Optional[list[AccessReviewScheduleDefinition]] = Field(alias="definitions", default=None,)
	historyDefinitions: Optional[list[AccessReviewHistoryDefinition]] = Field(alias="historyDefinitions", default=None,)

from .access_review_schedule_definition import AccessReviewScheduleDefinition
from .access_review_history_definition import AccessReviewHistoryDefinition
