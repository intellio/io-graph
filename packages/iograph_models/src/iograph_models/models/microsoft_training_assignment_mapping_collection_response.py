from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MicrosoftTrainingAssignmentMappingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[MicrosoftTrainingAssignmentMapping]] = Field(default=None,alias="value",)

from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping

