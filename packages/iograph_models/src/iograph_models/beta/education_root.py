from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationRoot(BaseModel):
	classes: Optional[list[EducationClass]] = Field(alias="classes", default=None,)
	me: Optional[EducationUser] = Field(alias="me", default=None,)
	reports: Optional[ReportsRoot] = Field(alias="reports", default=None,)
	schools: Optional[list[EducationSchool]] = Field(alias="schools", default=None,)
	users: Optional[list[EducationUser]] = Field(alias="users", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .education_class import EducationClass
from .education_user import EducationUser
from .reports_root import ReportsRoot
from .education_school import EducationSchool
