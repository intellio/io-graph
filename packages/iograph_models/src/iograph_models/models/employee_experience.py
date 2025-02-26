from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EmployeeExperience(BaseModel):
	communities: list[Community] = Field(alias="communities",)
	engagementAsyncOperations: list[EngagementAsyncOperation] = Field(alias="engagementAsyncOperations",)
	learningCourseActivities: list[LearningCourseActivity] = Field(alias="learningCourseActivities",)
	learningProviders: list[LearningProvider] = Field(alias="learningProviders",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .community import Community
from .engagement_async_operation import EngagementAsyncOperation
from .learning_course_activity import LearningCourseActivity
from .learning_provider import LearningProvider

