from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class TeamsAdministrationAssignedTelephoneNumber(BaseModel):
	assignmentCategory: Optional[TeamsAdministrationAssignmentCategory | str] = Field(alias="assignmentCategory", default=None,)
	telephoneNumber: Optional[str] = Field(alias="telephoneNumber", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .teams_administration_assignment_category import TeamsAdministrationAssignmentCategory
