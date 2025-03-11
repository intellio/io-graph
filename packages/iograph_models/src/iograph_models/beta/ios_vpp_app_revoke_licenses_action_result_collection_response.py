from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class IosVppAppRevokeLicensesActionResultCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count",default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink",default=None,)
	value: Optional[list[IosVppAppRevokeLicensesActionResult]] = Field(alias="value",default=None,)

from .ios_vpp_app_revoke_licenses_action_result import IosVppAppRevokeLicensesActionResult

