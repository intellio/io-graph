from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationRoot(BaseModel):
	classes: Optional[list[EducationClass]] = Field(default=None,alias="classes",)
	me: Optional[EducationUser] = Field(default=None,alias="me",)
	schools: Optional[list[EducationSchool]] = Field(default=None,alias="schools",)
	users: Optional[list[EducationUser]] = Field(default=None,alias="users",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_class import EducationClass
from .education_user import EducationUser
from .education_school import EducationSchool
from .education_user import EducationUser

