from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MfaTelecomFraudMetric(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	captchaFailureCount: Optional[int] = Field(alias="captchaFailureCount",default=None,)
	captchaNotTriggeredUserCount: Optional[int] = Field(alias="captchaNotTriggeredUserCount",default=None,)
	captchaShownUserCount: Optional[int] = Field(alias="captchaShownUserCount",default=None,)
	captchaSuccessCount: Optional[int] = Field(alias="captchaSuccessCount",default=None,)
	factDate: Optional[str] = Field(alias="factDate",default=None,)
	telecomBlockedUserCount: Optional[int] = Field(alias="telecomBlockedUserCount",default=None,)


