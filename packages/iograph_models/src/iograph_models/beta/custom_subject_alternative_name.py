from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CustomSubjectAlternativeName(BaseModel):
	name: Optional[str] = Field(alias="name",default=None,)
	sanType: Optional[SubjectAlternativeNameType | str] = Field(alias="sanType",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .subject_alternative_name_type import SubjectAlternativeNameType

