from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternal(BaseModel):
	authorizationSystems: SerializeAsAny[Optional[list[AuthorizationSystem]]] = Field(alias="authorizationSystems",default=None,)
	connections: Optional[list[ExternalConnectorsExternalConnection]] = Field(alias="connections",default=None,)
	industryData: Optional[IndustryDataIndustryDataRoot] = Field(alias="industryData",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .authorization_system import AuthorizationSystem
from .external_connectors_external_connection import ExternalConnectorsExternalConnection
from .industry_data_industry_data_root import IndustryDataIndustryDataRoot

