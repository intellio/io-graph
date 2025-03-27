from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternalConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)
	activitySettings: Optional[ExternalConnectorsActivitySettings] = Field(alias="activitySettings", default=None,)
	configuration: Optional[ExternalConnectorsConfiguration] = Field(alias="configuration", default=None,)
	connectorId: Optional[str] = Field(alias="connectorId", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	searchSettings: Optional[ExternalConnectorsSearchSettings] = Field(alias="searchSettings", default=None,)
	state: Optional[ExternalConnectorsConnectionState | str] = Field(alias="state", default=None,)
	groups: Optional[list[ExternalConnectorsExternalGroup]] = Field(alias="groups", default=None,)
	items: Optional[list[ExternalConnectorsExternalItem]] = Field(alias="items", default=None,)
	operations: Optional[list[ExternalConnectorsConnectionOperation]] = Field(alias="operations", default=None,)
	schema: Optional[ExternalConnectorsSchema] = Field(alias="schema", default=None,)

from .external_connectors_activity_settings import ExternalConnectorsActivitySettings
from .external_connectors_configuration import ExternalConnectorsConfiguration
from .external_connectors_search_settings import ExternalConnectorsSearchSettings
from .external_connectors_connection_state import ExternalConnectorsConnectionState
from .external_connectors_external_group import ExternalConnectorsExternalGroup
from .external_connectors_external_item import ExternalConnectorsExternalItem
from .external_connectors_connection_operation import ExternalConnectorsConnectionOperation
from .external_connectors_schema import ExternalConnectorsSchema

