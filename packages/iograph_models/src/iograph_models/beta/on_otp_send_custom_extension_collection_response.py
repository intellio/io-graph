from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnOtpSendCustomExtensionCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[OnOtpSendCustomExtension]] = Field(alias="value",default=None,)

from .on_otp_send_custom_extension import OnOtpSendCustomExtension

