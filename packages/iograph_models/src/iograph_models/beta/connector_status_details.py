from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class ConnectorStatusDetails(BaseModel):
	connectorInstanceId: Optional[str] = Field(alias="connectorInstanceId",default=None,)
	connectorName: Optional[ConnectorName | str] = Field(alias="connectorName",default=None,)
	eventDateTime: Optional[datetime] = Field(alias="eventDateTime",default=None,)
	status: Optional[ConnectorHealthState | str] = Field(alias="status",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .connector_name import ConnectorName
from .connector_health_state import ConnectorHealthState

