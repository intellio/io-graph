from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class SecurityAnalyzedEmailDeliveryDetail(BaseModel):
	action: Optional[SecurityDeliveryAction | str] = Field(alias="action", default=None,)
	latestThreats: Optional[str] = Field(alias="latestThreats", default=None,)
	location: Optional[SecurityDeliveryLocation | str] = Field(alias="location", default=None,)
	originalThreats: Optional[str] = Field(alias="originalThreats", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .security_delivery_action import SecurityDeliveryAction
from .security_delivery_location import SecurityDeliveryLocation

