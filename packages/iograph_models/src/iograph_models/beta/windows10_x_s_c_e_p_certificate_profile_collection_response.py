from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Windows10XSCEPCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[Windows10XSCEPCertificateProfile]] = Field(alias="value",default=None,)

from .windows10_x_s_c_e_p_certificate_profile import Windows10XSCEPCertificateProfile

