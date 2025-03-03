from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SendDtmfTonesOperationCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(default=None,alias="@odata.count",)
	odata_nextLink: Optional[str] = Field(default=None,alias="@odata.nextLink",)
	value: Optional[list[SendDtmfTonesOperation]] = Field(default=None,alias="value",)

from .send_dtmf_tones_operation import SendDtmfTonesOperation

