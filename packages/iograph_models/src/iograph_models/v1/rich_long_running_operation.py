from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class RichLongRunningOperation(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.richLongRunningOperation"] = Field(alias="@odata.type", default="#microsoft.graph.richLongRunningOperation")
	createdDateTime: Optional[datetime] = Field(alias="createdDateTime", default=None,)
	lastActionDateTime: Optional[datetime] = Field(alias="lastActionDateTime", default=None,)
	resourceLocation: Optional[str] = Field(alias="resourceLocation", default=None,)
	status: Optional[LongRunningOperationStatus | str] = Field(alias="status", default=None,)
	statusDetail: Optional[str] = Field(alias="statusDetail", default=None,)
	error: Optional[PublicError] = Field(alias="error", default=None,)
	percentageComplete: Optional[int] = Field(alias="percentageComplete", default=None,)
	resourceId: Optional[str] = Field(alias="resourceId", default=None,)
	type: Optional[str] = Field(alias="type", default=None,)

from .long_running_operation_status import LongRunningOperationStatus
from .public_error import PublicError
