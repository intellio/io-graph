from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationStudent(BaseModel):
	birthDate: Optional[str] = Field(default=None,alias="birthDate",)
	externalId: Optional[str] = Field(default=None,alias="externalId",)
	gender: Optional[EducationGender] = Field(default=None,alias="gender",)
	grade: Optional[str] = Field(default=None,alias="grade",)
	graduationYear: Optional[str] = Field(default=None,alias="graduationYear",)
	studentNumber: Optional[str] = Field(default=None,alias="studentNumber",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .education_gender import EducationGender

