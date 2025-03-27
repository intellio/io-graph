from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataEnrollmentMappings(BaseModel):
	memberEnrollmentMappings: Optional[list[IndustryDataSectionRoleReferenceValue]] = Field(alias="memberEnrollmentMappings", default=None,)
	ownerEnrollmentMappings: Optional[list[IndustryDataSectionRoleReferenceValue]] = Field(alias="ownerEnrollmentMappings", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .industry_data_section_role_reference_value import IndustryDataSectionRoleReferenceValue
from .industry_data_section_role_reference_value import IndustryDataSectionRoleReferenceValue

