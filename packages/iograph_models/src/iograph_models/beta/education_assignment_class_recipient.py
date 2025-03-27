from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentClassRecipient(BaseModel):
	odata_type: Literal["#microsoft.graph.educationAssignmentClassRecipient"] = Field(alias="@odata.type", default="#microsoft.graph.educationAssignmentClassRecipient")


