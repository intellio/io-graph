from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EducationAssignmentIndividualRecipient(BaseModel):
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	recipients: list[Optional[str]] = Field(alias="recipients",)


