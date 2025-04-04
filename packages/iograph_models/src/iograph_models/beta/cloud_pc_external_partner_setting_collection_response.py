from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class CloudPcExternalPartnerSettingCollectionResponse(BaseModel):
	odata_count: Optional[int] = Field(alias="@odata.count", default=None,)
	odata_nextLink: Optional[str] = Field(alias="@odata.nextLink", default=None,)
	value: Optional[list[CloudPcExternalPartnerSetting]] = Field(alias="value", default=None,)

from .cloud_pc_external_partner_setting import CloudPcExternalPartnerSetting
