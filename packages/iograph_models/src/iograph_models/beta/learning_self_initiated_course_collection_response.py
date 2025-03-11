from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LearningSelfInitiatedCourseCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[LearningSelfInitiatedCourse]] = Field(alias="value",default=None,)

from .learning_self_initiated_course import LearningSelfInitiatedCourse

