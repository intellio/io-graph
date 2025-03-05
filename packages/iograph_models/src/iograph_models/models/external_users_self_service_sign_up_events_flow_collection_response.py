from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class ExternalUsersSelfServiceSignUpEventsFlowCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[ExternalUsersSelfServiceSignUpEventsFlow]] = Field(default=None,alias="value",)

from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

