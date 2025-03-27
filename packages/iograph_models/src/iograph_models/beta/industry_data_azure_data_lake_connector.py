from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataAzureDataLakeConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.azureDataLakeConnector"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.azureDataLakeConnector")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sourceSystem: Optional[IndustryDataSourceSystemDefinition] = Field(alias="sourceSystem", default=None,)
	fileFormat: Optional[IndustryDataFileFormatReferenceValue] = Field(alias="fileFormat", default=None,)

from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_file_format_reference_value import IndustryDataFileFormatReferenceValue

