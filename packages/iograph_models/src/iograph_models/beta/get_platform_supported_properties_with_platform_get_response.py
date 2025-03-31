from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class Get_platform_supported_properties_with_platformGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AssignmentFilterSupportedProperty]] = Field(alias="value", default=None,)

from .assignment_filter_supported_property import AssignmentFilterSupportedProperty
