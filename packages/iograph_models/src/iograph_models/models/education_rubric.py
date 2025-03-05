from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationRubric(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="createdBy",)
	createdDateTime: Optional[datetime] = Field(default=None,alias="createdDateTime",)
	description: Optional[EducationItemBody] = Field(default=None,alias="description",)
	displayName: Optional[str] = Field(default=None,alias="displayName",)
	grading: SerializeAsAny[Optional[EducationAssignmentGradeType]] = Field(default=None,alias="grading",)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(default=None,alias="lastModifiedBy",)
	lastModifiedDateTime: Optional[datetime] = Field(default=None,alias="lastModifiedDateTime",)
	levels: Optional[list[RubricLevel]] = Field(default=None,alias="levels",)
	qualities: Optional[list[RubricQuality]] = Field(default=None,alias="qualities",)

from .identity_set import IdentitySet
from .education_item_body import EducationItemBody
from .education_assignment_grade_type import EducationAssignmentGradeType
from .identity_set import IdentitySet
from .rubric_level import RubricLevel
from .rubric_quality import RubricQuality

