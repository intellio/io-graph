from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class DelegateAllowedActions(BaseModel):
	joinActiveCalls: Optional[bool] = Field(alias="joinActiveCalls",default=None,)
	makeCalls: Optional[bool] = Field(alias="makeCalls",default=None,)
	manageCallAndDelegateSettings: Optional[bool] = Field(alias="manageCallAndDelegateSettings",default=None,)
	pickUpHeldCalls: Optional[bool] = Field(alias="pickUpHeldCalls",default=None,)
	receiveCalls: Optional[bool] = Field(alias="receiveCalls",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)


