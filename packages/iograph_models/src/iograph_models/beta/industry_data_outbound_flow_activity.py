from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IndustryDataOutboundFlowActivity(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	blockingError: Optional[PublicError] = Field(alias="blockingError",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	status: Optional[IndustryDataIndustryDataActivityStatus | str] = Field(alias="status",default=None,)
	activity: SerializeAsAny[Optional[IndustryDataIndustryDataActivity]] = Field(alias="activity",default=None,)

from .public_error import PublicError
from .industry_data_industry_data_activity_status import IndustryDataIndustryDataActivityStatus
from .industry_data_industry_data_activity import IndustryDataIndustryDataActivity

