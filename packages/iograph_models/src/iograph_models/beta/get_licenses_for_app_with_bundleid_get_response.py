from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Get_licenses_for_app_with_bundleidGetResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[VppTokenLicenseSummary]] = Field(alias="value", default=None,)

from .vpp_token_license_summary import VppTokenLicenseSummary

