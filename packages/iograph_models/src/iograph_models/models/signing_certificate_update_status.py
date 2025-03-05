from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SigningCertificateUpdateStatus(BaseModel):
	certificateUpdateResult: Optional[str] = Field(default=None,alias="certificateUpdateResult",)
	lastRunDateTime: Optional[datetime] = Field(default=None,alias="lastRunDateTime",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)


