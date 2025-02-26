from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationRoot(BaseModel):
	classes: list[EducationClass] = Field(alias="classes",)
	me: Optional[EducationUser] = Field(default=None,alias="me",)
	schools: list[EducationSchool] = Field(alias="schools",)
	users: list[EducationUser] = Field(alias="users",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_class import EducationClass
from .education_user import EducationUser
from .education_school import EducationSchool
from .education_user import EducationUser

