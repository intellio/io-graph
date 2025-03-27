from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class LearningCourseActivityCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[Annotated[Union[LearningAssignment, LearningSelfInitiatedCourse],Field(discriminator="odata_type")]]] = Field(alias="value", default=None,)

from .learning_assignment import LearningAssignment
from .learning_self_initiated_course import LearningSelfInitiatedCourse

