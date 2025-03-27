from __future__ import annotations
from typing import Optional
from typing import Union
from typing import Annotated
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternal(BaseModel):
	authorizationSystems: Optional[list[Annotated[Union[AwsAuthorizationSystem, AzureAuthorizationSystem, GcpAuthorizationSystem],Field(discriminator="odata_type")]]] = Field(alias="authorizationSystems", default=None,)
	connections: Optional[list[ExternalConnectorsExternalConnection]] = Field(alias="connections", default=None,)
	industryData: Optional[IndustryDataIndustryDataRoot] = Field(alias="industryData", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .aws_authorization_system import AwsAuthorizationSystem
from .azure_authorization_system import AzureAuthorizationSystem
from .gcp_authorization_system import GcpAuthorizationSystem
from .external_connectors_external_connection import ExternalConnectorsExternalConnection
from .industry_data_industry_data_root import IndustryDataIndustryDataRoot

