from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmployeeExperience(BaseModel):
	communities: Optional[list[Community]] = Field(default=None,alias="communities",)
	engagementAsyncOperations: Optional[list[EngagementAsyncOperation]] = Field(default=None,alias="engagementAsyncOperations",)
	learningCourseActivities: Optional[list[LearningCourseActivity]] = Field(default=None,alias="learningCourseActivities",)
	learningProviders: Optional[list[LearningProvider]] = Field(default=None,alias="learningProviders",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .community import Community
from .engagement_async_operation import EngagementAsyncOperation
from .learning_course_activity import LearningCourseActivity
from .learning_provider import LearningProvider

