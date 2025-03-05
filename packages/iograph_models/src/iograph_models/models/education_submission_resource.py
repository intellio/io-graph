from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EducationSubmissionResource(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	assignmentResourceUrl: Optional[str] = Field(alias="assignmentResourceUrl",default=None,)
	resource: SerializeAsAny[Optional[EducationResource]] = Field(alias="resource",default=None,)

from .education_resource import EducationResource

