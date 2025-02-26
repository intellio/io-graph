from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesAccidentalDeletionPrevention(BaseModel):
	alertThreshold: Optional[int] = Field(default=None,alias="alertThreshold",)
	synchronizationPreventionType: Optional[OnPremisesDirectorySynchronizationDeletionPreventionType] = Field(default=None,alias="synchronizationPreventionType",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)

from .on_premises_directory_synchronization_deletion_prevention_type import OnPremisesDirectorySynchronizationDeletionPreventionType

