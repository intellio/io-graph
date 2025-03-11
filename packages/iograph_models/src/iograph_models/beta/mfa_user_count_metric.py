from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class MfaUserCountMetric(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	count: Optional[int] = Field(alias="count",default=None,)
	factDate: Optional[str] = Field(alias="factDate",default=None,)
	mfaType: Optional[MfaType | str] = Field(alias="mfaType",default=None,)

from .mfa_type import MfaType

