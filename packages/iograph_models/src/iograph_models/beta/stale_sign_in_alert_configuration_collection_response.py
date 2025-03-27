from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class StaleSignInAlertConfigurationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[StaleSignInAlertConfiguration]] = Field(alias="value", default=None,)

from .stale_sign_in_alert_configuration import StaleSignInAlertConfiguration

