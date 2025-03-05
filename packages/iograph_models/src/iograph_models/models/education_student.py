from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationStudent(BaseModel):
	birthDate: Optional[str] = Field(alias="birthDate",default=None,)
	externalId: Optional[str] = Field(alias="externalId",default=None,)
	gender: Optional[EducationGender | str] = Field(alias="gender",default=None,)
	grade: Optional[str] = Field(alias="grade",default=None,)
	graduationYear: Optional[str] = Field(alias="graduationYear",default=None,)
	studentNumber: Optional[str] = Field(alias="studentNumber",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .education_gender import EducationGender

