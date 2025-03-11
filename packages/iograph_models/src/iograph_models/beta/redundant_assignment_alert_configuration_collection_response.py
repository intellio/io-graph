from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class RedundantAssignmentAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[RedundantAssignmentAlertConfiguration]] = Field(alias="value",default=None,)

from .redundant_assignment_alert_configuration import RedundantAssignmentAlertConfiguration

