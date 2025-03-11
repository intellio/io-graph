from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesQualityUpdateFilter(BaseModel):
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	cadence: Optional[WindowsUpdatesQualityUpdateCadence | str] = Field(alias="cadence",default=None,)
	classification: Optional[WindowsUpdatesQualityUpdateClassification | str] = Field(alias="classification",default=None,)

from .windows_updates_quality_update_cadence import WindowsUpdatesQualityUpdateCadence
from .windows_updates_quality_update_classification import WindowsUpdatesQualityUpdateClassification

