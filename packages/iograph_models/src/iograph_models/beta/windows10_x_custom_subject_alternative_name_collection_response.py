from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10XCustomSubjectAlternativeNameCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[Windows10XCustomSubjectAlternativeName]] = Field(alias="value",default=None,)

from .windows10_x_custom_subject_alternative_name import Windows10XCustomSubjectAlternativeName

