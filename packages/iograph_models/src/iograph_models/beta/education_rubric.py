from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class EducationRubric(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	createdBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="createdBy",default=None,)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime",default=None,)
	description: Optional[EducationItemBody] = Field(alias="description",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	grading: SerializeAsAny[Optional[EducationAssignmentGradeType]] = Field(alias="grading",default=None,)
	lastModifiedBy: SerializeAsAny[Optional[IdentitySet]] = Field(alias="lastModifiedBy",default=None,)
	lastModifiedDateTime: Optional[datetime] = Field(alias="lastModifiedDateTime",default=None,)
	levels: Optional[list[RubricLevel]] = Field(alias="levels",default=None,)
	qualities: Optional[list[RubricQuality]] = Field(alias="qualities",default=None,)

from .identity_set import IdentitySet
from .education_item_body import EducationItemBody
from .education_assignment_grade_type import EducationAssignmentGradeType
from .identity_set import IdentitySet
from .rubric_level import RubricLevel
from .rubric_quality import RubricQuality

