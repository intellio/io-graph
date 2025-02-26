from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class EnrollmentConfigurationAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: list[EnrollmentConfigurationAssignment] = Field(alias="value",)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

