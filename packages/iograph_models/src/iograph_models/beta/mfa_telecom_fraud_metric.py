from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class MfaTelecomFraudMetric(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.mfaTelecomFraudMetric"] = Field(alias="@odata.type", default="#microsoft.graph.mfaTelecomFraudMetric")
	captchaFailureCount: Optional[int] = Field(alias="captchaFailureCount", default=None,)
	captchaNotTriggeredUserCount: Optional[int] = Field(alias="captchaNotTriggeredUserCount", default=None,)
	captchaShownUserCount: Optional[int] = Field(alias="captchaShownUserCount", default=None,)
	captchaSuccessCount: Optional[int] = Field(alias="captchaSuccessCount", default=None,)
	factDate: Optional[str] = Field(alias="factDate", default=None,)
	telecomBlockedUserCount: Optional[int] = Field(alias="telecomBlockedUserCount", default=None,)

