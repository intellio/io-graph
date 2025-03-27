from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field, SerializeAsAny


class OnPremisesDirectorySynchronizationConfiguration(BaseModel):
	accidentalDeletionPrevention: Optional[OnPremisesAccidentalDeletionPrevention] = Field(alias="accidentalDeletionPrevention", default=None,)
	anchorAttribute: Optional[str] = Field(alias="anchorAttribute", default=None,)
	applicationId: Optional[str] = Field(alias="applicationId", default=None,)
	currentExportData: Optional[OnPremisesCurrentExportData] = Field(alias="currentExportData", default=None,)
	customerRequestedSynchronizationInterval: Optional[str] = Field(alias="customerRequestedSynchronizationInterval", default=None,)
	synchronizationClientVersion: Optional[str] = Field(alias="synchronizationClientVersion", default=None,)
	synchronizationInterval: Optional[str] = Field(alias="synchronizationInterval", default=None,)
	writebackConfiguration: Optional[OnPremisesWritebackConfiguration] = Field(alias="writebackConfiguration", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .on_premises_accidental_deletion_prevention import OnPremisesAccidentalDeletionPrevention
from .on_premises_current_export_data import OnPremisesCurrentExportData
from .on_premises_writeback_configuration import OnPremisesWritebackConfiguration

