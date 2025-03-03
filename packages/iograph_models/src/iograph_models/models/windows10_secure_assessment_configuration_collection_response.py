from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Windows10SecureAssessmentConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[Windows10SecureAssessmentConfiguration]] = Field(default=None,alias="value",)

from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

