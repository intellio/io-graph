from __future__ import annotations
from typing import Optional
from typing import Literal
from datetime import datetime
from pydantic import BaseModel, Field


class MacOSSoftwareUpdateStateSummary(BaseModel):
	id: Optional[str] = Field(alias="id", default=None,)
	odata_type: Literal["#microsoft.graph.macOSSoftwareUpdateStateSummary"] = Field(alias="@odata.type", default="#microsoft.graph.macOSSoftwareUpdateStateSummary")
	displayName: Optional[str] = Field(alias="displayName", default=None,)
	lastUpdatedDateTime: Optional[datetime] = Field(alias="lastUpdatedDateTime", default=None,)
	productKey: Optional[str] = Field(alias="productKey", default=None,)
	state: Optional[MacOSSoftwareUpdateState | str] = Field(alias="state", default=None,)
	updateCategory: Optional[MacOSSoftwareUpdateCategory | str] = Field(alias="updateCategory", default=None,)
	updateVersion: Optional[str] = Field(alias="updateVersion", default=None,)

from .mac_o_s_software_update_state import MacOSSoftwareUpdateState
from .mac_o_s_software_update_category import MacOSSoftwareUpdateCategory
