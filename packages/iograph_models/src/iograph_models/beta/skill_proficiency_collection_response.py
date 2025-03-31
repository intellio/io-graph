from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SkillProficiencyCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[SkillProficiency]] = Field(alias="value", default=None,)

from .skill_proficiency import SkillProficiency
