from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EmployeeExperience(BaseModel):
	communities: Optional[list[Community]] = Field(alias="communities",default=None,)
	engagementAsyncOperations: Optional[list[EngagementAsyncOperation]] = Field(alias="engagementAsyncOperations",default=None,)
	goals: Optional[Goals] = Field(alias="goals",default=None,)
	learningCourseActivities: SerializeAsAny[Optional[list[LearningCourseActivity]]] = Field(alias="learningCourseActivities",default=None,)
	learningProviders: Optional[list[LearningProvider]] = Field(alias="learningProviders",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .community import Community
from .engagement_async_operation import EngagementAsyncOperation
from .goals import Goals
from .learning_course_activity import LearningCourseActivity
from .learning_provider import LearningProvider

