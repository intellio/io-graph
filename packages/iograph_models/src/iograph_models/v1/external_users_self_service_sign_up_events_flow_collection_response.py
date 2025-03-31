from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[ExternalUsersSelfServiceSignUpEventsFlow]] = Field(alias="value", default=None,)

from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
