from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class IndustryDataAdditionalUserOptions(BaseModel):
	allowStudentContactAssociation: Optional[bool] = Field(alias="allowStudentContactAssociation", default=None,)
	markAllStudentsAsMinors: Optional[bool] = Field(alias="markAllStudentsAsMinors", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

