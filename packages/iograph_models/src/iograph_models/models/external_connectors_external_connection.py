from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalConnectorsExternalConnection(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	activitySettings: Optional[ExternalConnectorsActivitySettings] = Field(default=None,alias="activitySettings",)
	configuration: Optional[ExternalConnectorsConfiguration] = Field(default=None,alias="configuration",)
	connectorId: Optional[str] = Field(default=None,alias="connectorId",)
	description: Optional[str] = Field(default=None,alias="description",)
	name: Optional[str] = Field(default=None,alias="name",)
	searchSettings: Optional[ExternalConnectorsSearchSettings] = Field(default=None,alias="searchSettings",)
	state: Optional[ExternalConnectorsConnectionState] = Field(default=None,alias="state",)
	groups: Optional[list[ExternalConnectorsExternalGroup]] = Field(default=None,alias="groups",)
	items: Optional[list[ExternalConnectorsExternalItem]] = Field(default=None,alias="items",)
	operations: Optional[list[ExternalConnectorsConnectionOperation]] = Field(default=None,alias="operations",)
	schema: Optional[ExternalConnectorsSchema] = Field(default=None,alias="schema",)

from .external_connectors_activity_settings import ExternalConnectorsActivitySettings
from .external_connectors_configuration import ExternalConnectorsConfiguration
from .external_connectors_search_settings import ExternalConnectorsSearchSettings
from .external_connectors_connection_state import ExternalConnectorsConnectionState
from .external_connectors_external_group import ExternalConnectorsExternalGroup
from .external_connectors_external_item import ExternalConnectorsExternalItem
from .external_connectors_connection_operation import ExternalConnectorsConnectionOperation
from .external_connectors_schema import ExternalConnectorsSchema

