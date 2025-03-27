from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class EnrollmentConfigurationAssignmentCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[EnrollmentConfigurationAssignment]] = Field(alias="value", default=None,)

from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

