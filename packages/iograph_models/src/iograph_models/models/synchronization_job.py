from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field


class SynchronizationJob(BaseModel):
	id: Optional[str] = Field(default=None,alias="id",)
	odata_type: Optional[str] = Field(default=None,alias="@odata.type",)
	schedule: Optional[SynchronizationSchedule] = Field(default=None,alias="schedule",)
	status: Optional[SynchronizationStatus] = Field(default=None,alias="status",)
	synchronizationJobSettings: list[KeyValuePair] = Field(alias="synchronizationJobSettings",)
	templateId: Optional[str] = Field(default=None,alias="templateId",)
	bulkUpload: Optional[BulkUpload] = Field(default=None,alias="bulkUpload",)
	schema: Optional[SynchronizationSchema] = Field(default=None,alias="schema",)

from .synchronization_schedule import SynchronizationSchedule
from .synchronization_status import SynchronizationStatus
from .key_value_pair import KeyValuePair
from .bulk_upload import BulkUpload
from .synchronization_schema import SynchronizationSchema

