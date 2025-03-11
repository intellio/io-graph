from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataFileFormatReferenceValue(BaseModel):
	code: Optional[str] = Field(alias="code",default=None,)
	value: Optional[IndustryDataReferenceDefinition] = Field(alias="value",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .industry_data_reference_definition import IndustryDataReferenceDefinition

