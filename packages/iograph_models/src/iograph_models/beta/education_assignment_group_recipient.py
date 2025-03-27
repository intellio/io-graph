from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentGroupRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.educationAssignmentGroupRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentGroupRecipient")


