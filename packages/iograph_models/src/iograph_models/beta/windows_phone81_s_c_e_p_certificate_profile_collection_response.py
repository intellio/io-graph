from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsPhone81SCEPCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[WindowsPhone81SCEPCertificateProfile]] = Field(alias="value",default=None,)

from .windows_phone81_s_c_e_p_certificate_profile import WindowsPhone81SCEPCertificateProfile

