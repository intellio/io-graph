from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataSectionRoleReferenceValueCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IndustryDataSectionRoleReferenceValue]] = Field(alias="value",default=None,)

from .industry_data_section_role_reference_value import IndustryDataSectionRoleReferenceValue

