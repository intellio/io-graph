from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataClassGroupConfiguration(BaseModel):
	additionalAttributes: Optional[IndustryDataAdditionalClassGroupAttributes | str] = Field(alias="additionalAttributes",default=None,)
	additionalOptions: Optional[IndustryDataAdditionalClassGroupOptions] = Field(alias="additionalOptions",default=None,)
	enrollmentMappings: Optional[IndustryDataEnrollmentMappings] = Field(alias="enrollmentMappings",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .industry_data_additional_class_group_attributes import IndustryDataAdditionalClassGroupAttributes
from .industry_data_additional_class_group_options import IndustryDataAdditionalClassGroupOptions
from .industry_data_enrollment_mappings import IndustryDataEnrollmentMappings

