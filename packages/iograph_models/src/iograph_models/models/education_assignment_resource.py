from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationAssignmentResource(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	distributeForStudentWork: Optional[bool] = Field(default=None,alias="distributeForStudentWork",)
	resource: SerializeAsAny[Optional[EducationResource]] = Field(default=None,alias="resource",)

from .education_resource import EducationResource

