from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class CloudPcResizeValidationResult(BaseModel):
	cloudPcId: Optional[str] = Field(alias="cloudPcId",default=None,)
	validationResult: Optional[CloudPcResizeValidationCode | str] = Field(alias="validationResult",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)

from .cloud_pc_resize_validation_code import CloudPcResizeValidationCode

