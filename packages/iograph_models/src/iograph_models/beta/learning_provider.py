from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from typing import Annotated
from pydantic import BaseModel, Field


class LearningProvider(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.learningProvider"] = Field(alias="@odata.type", default="#microsoft.graph.learningProvider")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	isCourseActivitySyncEnabled: Optional[bool] = Field(alias="isCourseActivitySyncEnabled", default=None,)
	loginWebUrl: Optional[str] = Field(alias="loginWebUrl", default=None,)
	longLogoWebUrlForDarkTheme: Optional[str] = Field(alias="longLogoWebUrlForDarkTheme", default=None,)
	longLogoWebUrlForLightTheme: Optional[str] = Field(alias="longLogoWebUrlForLightTheme", default=None,)
	squareLogoWebUrlForDarkTheme: Optional[str] = Field(alias="squareLogoWebUrlForDarkTheme", default=None,)
	squareLogoWebUrlForLightTheme: Optional[str] = Field(alias="squareLogoWebUrlForLightTheme", default=None,)
	learningContents: Optional[list[LearningContent]] = Field(alias="learningContents", default=None,)
	learningCourseActivities: Optional[list[Annotated[Union[LearningAssignment, LearningSelfInitiatedCourse],Field(discriminator="odata_type")]]] = Field(alias="learningCourseActivities", default=None,)

from .learning_content import LearningContent
from .learning_assignment import LearningAssignment
from .learning_self_initiated_course import LearningSelfInitiatedCourse
