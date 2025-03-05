from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class LearningProvider(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	isCourseActivitySyncEnabled: Optional[bool] = Field(alias="isCourseActivitySyncEnabled",default=None,)
	loginWebUrl: Optional[str] = Field(alias="loginWebUrl",default=None,)
	longLogoWebUrlForDarkTheme: Optional[str] = Field(alias="longLogoWebUrlForDarkTheme",default=None,)
	longLogoWebUrlForLightTheme: Optional[str] = Field(alias="longLogoWebUrlForLightTheme",default=None,)
	squareLogoWebUrlForDarkTheme: Optional[str] = Field(alias="squareLogoWebUrlForDarkTheme",default=None,)
	squareLogoWebUrlForLightTheme: Optional[str] = Field(alias="squareLogoWebUrlForLightTheme",default=None,)
	learningContents: Optional[list[LearningContent]] = Field(alias="learningContents",default=None,)
	learningCourseActivities: SerializeAsAny[Optional[list[LearningCourseActivity]]] = Field(alias="learningCourseActivities",default=None,)

from .learning_content import LearningContent
from .learning_course_activity import LearningCourseActivity

