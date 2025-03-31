from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class ConnectorGroup(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.connectorGroup"] = Field(alias="@odata.type",)
	connectorGroupType: Optional[ConnectorGroupType | str] = Field(alias="connectorGroupType", default=None,)
	isDefault: Optional[bool] = Field(alias="isDefault", default=None,)
	name: Optional[str] = Field(alias="name", default=None,)
	region: Optional[ConnectorGroupRegion | str] = Field(alias="region", default=None,)
	applications: Optional[list[Application]] = Field(alias="applications", default=None,)
	members: Optional[list[Connector]] = Field(alias="members", default=None,)

from .connector_group_type import ConnectorGroupType
from .connector_group_region import ConnectorGroupRegion
from .application import Application
from .connector import Connector
