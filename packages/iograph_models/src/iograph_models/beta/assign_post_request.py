from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class AssignPostRequest(BaseModel):
	enrollmentConfigurationAssignments: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="enrollmentConfigurationAssignments", default=None,)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
