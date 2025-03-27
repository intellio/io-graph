from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidDeviceComplianceLocalActionLockDeviceWithPasscode(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode"] = Field(alias="@odata.type", default="#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode")
	gracePeriodInMinutes: Optional[int] = Field(alias="gracePeriodInMinutes", default=None,)
	passcode: Optional[str] = Field(alias="passcode", default=None,)
	passcodeSignInFailureCountBeforeWipe: Optional[int] = Field(alias="passcodeSignInFailureCountBeforeWipe", default=None,)


