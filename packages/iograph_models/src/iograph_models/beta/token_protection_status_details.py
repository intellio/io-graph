from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class TokenProtectionStatusDetails(BaseModel):
	signInSessionStatus: Optional[TokenProtectionStatus | str] = Field(alias="signInSessionStatus",default=None,)
	signInSessionStatusCode: Optional[int] = Field(alias="signInSessionStatusCode",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .token_protection_status import TokenProtectionStatus

