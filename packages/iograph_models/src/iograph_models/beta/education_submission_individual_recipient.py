from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class EducationSubmissionIndividualRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.educationSubmissionIndividualRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.educationSubmissionIndividualRecipient")
	userId: Optional[str] = Field(alias="userId", default=None,)

