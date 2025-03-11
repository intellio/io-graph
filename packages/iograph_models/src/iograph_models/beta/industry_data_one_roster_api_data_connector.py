from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOneRosterApiDataConnector(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	sourceSystem: Optional[IndustryDataSourceSystemDefinition] = Field(alias="sourceSystem",default=None,)
	apiFormat: Optional[IndustryDataApiFormat | str] = Field(alias="apiFormat",default=None,)
	baseUrl: Optional[str] = Field(alias="baseUrl",default=None,)
	credential: SerializeAsAny[Optional[IndustryDataCredential]] = Field(alias="credential",default=None,)
	apiVersion: Optional[str] = Field(alias="apiVersion",default=None,)
	isContactsEnabled: Optional[bool] = Field(alias="isContactsEnabled",default=None,)
	isDemographicsEnabled: Optional[bool] = Field(alias="isDemographicsEnabled",default=None,)
	isFlagsEnabled: Optional[bool] = Field(alias="isFlagsEnabled",default=None,)

from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_api_format import IndustryDataApiFormat
from .industry_data_credential import IndustryDataCredential

