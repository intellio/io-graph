from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TrainingNotificationDelivery(BaseModel):
	failedMessageDeliveryCount: Optional[int] = Field(alias="failedMessageDeliveryCount",default=None,)
	resolvedTargetsCount: Optional[int] = Field(alias="resolvedTargetsCount",default=None,)
	successfulMessageDeliveryCount: Optional[int] = Field(alias="successfulMessageDeliveryCount",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


