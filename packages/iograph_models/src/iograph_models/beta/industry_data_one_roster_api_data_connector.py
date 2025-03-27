from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOneRosterApiDataConnector(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.industryData.oneRosterApiDataConnector"] = Field(alias="@odata.type", default="#microsoft.graph.industryData.oneRosterApiDataConnector")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	sourceSystem: Optional[IndustryDataSourceSystemDefinition] = Field(alias="sourceSystem", default=None,)
	apiFormat: Optional[IndustryDataApiFormat | str] = Field(alias="apiFormat", default=None,)
	baseUrl: Optional[str] = Field(alias="baseUrl", default=None,)
	credential: Optional[Union[IndustryDataOAuthClientCredential, IndustryDataOAuth1ClientCredential, IndustryDataOAuth2ClientCredential]] = Field(alias="credential", default=None,discriminator="odata_type", )
	apiVersion: Optional[str] = Field(alias="apiVersion", default=None,)
	isContactsEnabled: Optional[bool] = Field(alias="isContactsEnabled", default=None,)
	isDemographicsEnabled: Optional[bool] = Field(alias="isDemographicsEnabled", default=None,)
	isFlagsEnabled: Optional[bool] = Field(alias="isFlagsEnabled", default=None,)

from .industry_data_source_system_definition import IndustryDataSourceSystemDefinition
from .industry_data_api_format import IndustryDataApiFormat
from .industry_data_o_auth_client_credential import IndustryDataOAuthClientCredential
from .industry_data_o_auth1_client_credential import IndustryDataOAuth1ClientCredential
from .industry_data_o_auth2_client_credential import IndustryDataOAuth2ClientCredential

