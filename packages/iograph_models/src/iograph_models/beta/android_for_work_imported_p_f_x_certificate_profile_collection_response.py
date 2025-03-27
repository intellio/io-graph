from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class AndroidForWorkImportedPFXCertificateProfileCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[AndroidForWorkImportedPFXCertificateProfile]] = Field(alias="value", default=None,)

from .android_for_work_imported_p_f_x_certificate_profile import AndroidForWorkImportedPFXCertificateProfile

