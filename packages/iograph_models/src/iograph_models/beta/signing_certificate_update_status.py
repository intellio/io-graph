from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class SigningCertificateUpdateStatus(BaseModel):
	certificateUpdateResult: Optional[str] = Field(alias="certificateUpdateResult", default=None,)
	lastRunDateTime: Optional[datetime] = Field(alias="lastRunDateTime", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)


