from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class Win32LobAppProductCodeDetection(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	productCode: Optional[str] = Field(alias="productCode",default=None,)
	productVersion: Optional[str] = Field(alias="productVersion",default=None,)
	productVersionOperator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="productVersionOperator",default=None,)

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator

