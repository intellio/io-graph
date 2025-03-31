from __future__ import annotations
from typing import Optional
from typing import Literal
from pydantic import BaseModel, Field


class Win32LobAppProductCodeDetection(BaseModel):
	odata_type: Literal["#microsoft.graph.win32LobAppProductCodeDetection"] = Field(alias="@odata.type", default="#microsoft.graph.win32LobAppProductCodeDetection")
	productCode: Optional[str] = Field(alias="productCode", default=None,)
	productVersion: Optional[str] = Field(alias="productVersion", default=None,)
	productVersionOperator: Optional[Win32LobAppDetectionOperator | str] = Field(alias="productVersionOperator", default=None,)

from .win32_lob_app_detection_operator import Win32LobAppDetectionOperator
