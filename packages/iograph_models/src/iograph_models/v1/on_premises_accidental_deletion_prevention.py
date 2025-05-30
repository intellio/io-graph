from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class OnPremisesAccidentalDeletionPrevention(BaseModel):
	alertThreshold: Optional[int] = Field(alias="alertThreshold", default=None,)
	synchronizationPreventionType: Optional[OnPremisesDirectorySynchronizationDeletionPreventionType | str] = Field(alias="synchronizationPreventionType", default=None,)
	odata_type: Optional[str] = Field(alias="@odata.type", default=None,)

from .on_premises_directory_synchronization_deletion_prevention_type import OnPremisesDirectorySynchronizationDeletionPreventionType
