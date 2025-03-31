from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CallRecordsPstnOnlineMeetingDialoutReport(BaseModel):
	currency: Optional[str] = Field(alias="currency", default=None,)
	destinationContext: Optional[str] = Field(alias="destinationContext", default=None,)
	totalCallCharge: Optional[int] = Field(alias="totalCallCharge", default=None,)
	totalCalls: Optional[int] = Field(alias="totalCalls", default=None,)
	totalCallSeconds: Optional[int] = Field(alias="totalCallSeconds", default=None,)
	usageLocation: Optional[str] = Field(alias="usageLocation", default=None,)
	userDisplayName: Optional[str] = Field(alias="userDisplayName", default=None,)
	userId: Optional[str] = Field(alias="userId", default=None,)
	userPrincipalName: Optional[str] = Field(alias="userPrincipalName", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

