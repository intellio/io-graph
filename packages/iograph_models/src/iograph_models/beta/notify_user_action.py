from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class NotifyUserAction(BaseModel):
	odata_type: Literal["#microsoft.graph.notifyUserAction"] = Field(alias="@odata.type",)
	actionLastModifiedDateTime: Optional[datetime] = Field(alias="actionLastModifiedDateTime", default=None,)
	emailText: Optional[str] = Field(alias="emailText", default=None,)
	policyTip: Optional[str] = Field(alias="policyTip", default=None,)
	recipients: Optional[list[str]] = Field(alias="recipients", default=None,)

