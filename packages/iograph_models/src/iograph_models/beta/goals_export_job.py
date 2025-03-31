from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class GoalsExportJob(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.goalsExportJob"] = Field(alias="@odata.type",)
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)
	statusDetail: Optional[str] = Field(alias="statusDetail", default=None,)
	content: Optional[str] = Field(alias="content", default=None,)
	expirationDateTime: Optional[datetime] = Field(alias="expirationDateTime", default=None,)
	explorerViewId: Optional[str] = Field(alias="explorerViewId", default=None,)
	goalsOrganizationId: Optional[str] = Field(alias="goalsOrganizationId", default=None,)

from .long_running_operation_status import LongRunningOperationStatus
