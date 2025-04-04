from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationAssignmentIndividualRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.educationAssignmentIndividualRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentIndividualRecipient")
	recipients: Optional[list[str]] = Field(alias="recipients", default=None,)

