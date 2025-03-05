from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10SecureAssessmentConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[Windows10SecureAssessmentConfiguration]] = Field(alias="value",default=None,)

from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

