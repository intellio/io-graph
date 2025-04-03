from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class PermissionsRequestChange(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.permissionsRequestChange"] = Field(alias="@odata.type", default="#microsoft.graph.permissionsRequestChange")
	activeOccurrenceStatus: Optional[PermissionsRequestOccurrenceStatus | str] = Field(alias="activeOccurrenceStatus", default=None,)
	modificationDateTime: Optional[datetime] = Field(alias="modificationDateTime", default=None,)
	permissionsRequestId: Optional[str] = Field(alias="permissionsRequestId", default=None,)
	statusDetail: Optional[StatusDetail | str] = Field(alias="statusDetail", default=None,)
	ticketId: Optional[str] = Field(alias="ticketId", default=None,)

from .permissions_request_occurrence_status import PermissionsRequestOccurrenceStatus
from .status_detail import StatusDetail
