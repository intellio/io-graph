from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ExternalConnection(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.externalConnection"] = Field(alias="@odata.type", default="#microsoft.graph.externalConnection")
	configuration: Optional[Configuration] = Field(alias="configuration", default=None,)
	description: Optional[str] = Field(alias="description", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	state: Optional[ConnectionState | str] = Field(alias="state", default=None,)
	groups: Optional[list[ExternalGroup]] = Field(alias="groups", default=None,)
	items: Optional[list[ExternalItem]] = Field(alias="items", default=None,)
	operations: Optional[list[ConnectionOperation]] = Field(alias="operations", default=None,)
	schema_: Optional[Schema] = Field(alias="schema", default=None,)

from .configuration import Configuration
from .connection_state import ConnectionState
from .external_group import ExternalGroup
from .external_item import ExternalItem
from .connection_operation import ConnectionOperation
from .schema import Schema
