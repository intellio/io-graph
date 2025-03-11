from __future__ import annotations
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, SerializeAsAny


class WindowsUpdatesQualityUpdateCatalogEntry(BaseModel):
	id: Optional[str] = Field(alias="id",default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type",default=None,)
	deployableUntilDateTime: Optional[datetime] = Field(alias="deployableUntilDateTime",default=None,)
	displayName: Optional[str] = Field(alias="displayName",default=None,)
	releaseDateTime: Optional[datetime] = Field(alias="releaseDateTime",default=None,)
	catalogName: Optional[str] = Field(alias="catalogName",default=None,)
	cveSeverityInformation: Optional[WindowsUpdatesQualityUpdateCveSeverityInformation] = Field(alias="cveSeverityInformation",default=None,)
	isExpeditable: Optional[bool] = Field(alias="isExpeditable",default=None,)
	qualityUpdateCadence: Optional[WindowsUpdatesQualityUpdateCadence | str] = Field(alias="qualityUpdateCadence",default=None,)
	qualityUpdateClassification: Optional[WindowsUpdatesQualityUpdateClassification | str] = Field(alias="qualityUpdateClassification",default=None,)
	shortName: Optional[str] = Field(alias="shortName",default=None,)
	productRevisions: Optional[list[WindowsUpdatesProductRevision]] = Field(alias="productRevisions",default=None,)

from .windows_updates_quality_update_cve_severity_information import WindowsUpdatesQualityUpdateCveSeverityInformation
from .windows_updates_quality_update_cadence import WindowsUpdatesQualityUpdateCadence
from .windows_updates_quality_update_classification import WindowsUpdatesQualityUpdateClassification
from .windows_updates_product_revision import WindowsUpdatesProductRevision

