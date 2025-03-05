from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LearningProvider(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	isCourseActivitySyncEnabled: Optional[bool] = Field(default=None,alias="isCourseActivitySyncEnabled",)
	loginWebUrl: Optional[str] = Field(default=None,alias="loginWebUrl",)
	longLogoWebUrlForDarkTheme: Optional[str] = Field(default=None,alias="longLogoWebUrlForDarkTheme",)
	longLogoWebUrlForLightTheme: Optional[str] = Field(default=None,alias="longLogoWebUrlForLightTheme",)
	squareLogoWebUrlForDarkTheme: Optional[str] = Field(default=None,alias="squareLogoWebUrlForDarkTheme",)
	squareLogoWebUrlForLightTheme: Optional[str] = Field(default=None,alias="squareLogoWebUrlForLightTheme",)
	learningContents: Optional[list[LearningContent]] = Field(default=None,alias="learningContents",)
	learningCourseActivities: Optional[list[LearningCourseActivity]] = Field(default=None,alias="learningCourseActivities",)

from .learning_content import LearningContent
from .learning_course_activity import LearningCourseActivity

