from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class UserPFXCertificateCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[UserPFXCertificate]] = Field(alias="value", default=None,)

from .user_p_f_x_certificate import UserPFXCertificate
