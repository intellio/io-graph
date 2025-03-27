from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class EmployeeExperience(BaseModel):
	communities: Optional[list[Community]] = Field(alias="communities", default=None,)
	engagementAsyncOperations: Optional[list[EngagementAsyncOperation]] = Field(alias="engagementAsyncOperations", default=None,)
	learningCourseActivities: Optional[list[Annotated[Union[LearningAssignment, LearningSelfInitiatedCourse],Field(discriminator="odata_type")]]] = Field(alias="learningCourseActivities", default=None,)
	learningProviders: Optional[list[LearningProvider]] = Field(alias="learningProviders", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .community import Community
from .engagement_async_operation import EngagementAsyncOperation
from .learning_assignment import LearningAssignment
from .learning_self_initiated_course import LearningSelfInitiatedCourse
from .learning_provider import LearningProvider

